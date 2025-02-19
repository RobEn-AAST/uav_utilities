# useful linux commands:
ip a flush enp44s0
sudo ip addr add 192.168.1.24/24 dev enp44s0
sudo ip link set enp44s0 up

# to use dhclient:
sudo dhclient enp44s0