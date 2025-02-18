from pymavlink import mavutil

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

def main():
    """Main function to define parameters and start upload."""
    port = "COM3"  # Change to your actual port (e.g., '/dev/ttyUSB0' on Linux)
    baudrate = 57600
    
    parameters = {
        "WP_RADIUS": 5.0,
        "RTL_ALT": 100.0,
        "LOITER_TIME": 3.0
    }
    
    upload_parameters(port, baudrate, parameters)

if __name__ == "__main__":
    main()
