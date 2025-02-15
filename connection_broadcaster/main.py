import subprocess

# COM = "/dev/ttyACM0" # for usb connection on linux systems
COM = "/dev/ttyUSB0" # for do3 connection on linux system

PORT = "14550"
BAUDRATE = "115200"

SWITCH_SUBNET = "192.168.1"


def add_mavproxy_output(ip_list):
    command = f"mavproxy.py --master={COM} " + " ".join([f"--out=udp:{SWITCH_SUBNET}.{ip}:{PORT}" for ip in ip_list]) + f" --out=udp:127.0.0.1:{PORT} --baudrate={BAUDRATE}"

    print("RUNNING----")
    subprocess.run(command, shell=True, check=True)

ips_list = range(5, 25)
add_mavproxy_output(ips_list)