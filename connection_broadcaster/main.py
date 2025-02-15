import subprocess

# COM = "/dev/ttyACM0"
COM = "/dev/ttyUSB0"

PORT = "14550"
BAUDRATE = "115200"

SWITCH_SUBNET = "192.168.1"


def add_mavproxy_output(ip_list):
    command = f"mavproxy.py --master={COM} " + " ".join([f"--out=udp:{SWITCH_SUBNET}.{ip}:{PORT}" for ip in ip_list]) + f" --out=udp:127.0.0.1:{PORT} --baudrate={BAUDRATE}"

    print("RUNNING----")
    subprocess.run(command, shell=True, check=True)

add_mavproxy_output(range(5, 255))