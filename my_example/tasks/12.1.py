import subprocess
from tabulate import tabulate

ip_lst = ["77.88.8.8", "192.168.10.1"]

def ping_ip_addresses(ip):
    for item in ip:
        subprocess.run(f"ping -n 1 {item}")


if __name__ == "__main__":
    ping_ip_addresses(ip_lst)

    sh_ip_int_br = [('FastEthernet0/0', '15.0.15.1', 'up', 'up'),
                ('FastEthernet0/1', '10.0.12.1', 'up', 'up'),
                ('FastEthernet0/2', '10.0.13.1', 'up', 'up'),
                ('Loopback0', '10.1.1.1', 'up', 'up'),
                ('Loopback100', '100.0.0.1', 'up', 'up')]
    
    print(tabulate(sh_ip_int_br))

    columns = ['Interface', 'IP', 'Status', 'Protocol']
    print(tabulate(sh_ip_int_br, headers=columns))

