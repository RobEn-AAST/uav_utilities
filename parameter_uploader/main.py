from pymavlink import mavutil
import yaml
import os

# SPECIFY THE PARAMS YOU WANT TO LOAD
load_sections = ["failsafe_full_disable", "preflight_sensor_checks", "takeoff", "here2"]
port = "/dev/ttyUSB0"
baudrate = 57600


current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "parameters", "params.yaml")

def set_parameter(connection, param_name, param_value):
    """Send a parameter to the flight controller."""
    connection.mav.param_set_send(
        connection.target_system, connection.target_component,
        param_name.encode(), float(param_value), mavutil.mavlink.MAV_PARAM_TYPE_REAL32
    )
    print(f"Setting {param_name} to {param_value}")

def upload_parameters(port, baudrate, parameters):
    """Connect to the flight controller and upload parameters."""
    print(f"Connecting to {port} at {baudrate} baud...")
    connection = mavutil.mavlink_connection(port, baud=baudrate)
    
    print("Waiting for heartbeat...")
    connection.wait_heartbeat()
    print(f"Connected to system {connection.target_system}, component {connection.target_component}")
    
    for param_name, param_value in parameters.items():
        set_parameter(connection, param_name, param_value)
    
    print("All parameters uploaded successfully.")

def load_parameters_from_yaml():
    """Load parameters from YAML file based on specified sections."""
    with open(file_path, 'r') as file:
        yaml_data = yaml.safe_load(file)
    
    parameters = {}
    for section in load_sections:
        if section in yaml_data:
            parameters.update(yaml_data[section])
        else:
            print(f"Warning: Section '{section}' not found in YAML file")
    
    return parameters

def main():
    """Main function to load parameters and start upload."""
    # Load parameters from YAML file
    parameters = load_parameters_from_yaml()
    
    if parameters:
        print(f"Loaded {len(parameters)} parameters from {len(load_sections)} sections")
        upload_parameters(port, baudrate, parameters)
    else:
        print("No parameters loaded. Check your YAML file and section names.")

if __name__ == "__main__":
    main()
