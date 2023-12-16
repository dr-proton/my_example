import netmiko

cisco_router = {
    'device_type': 'cisco_ios',
    'host': '192.168.177.161',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco',
    'port': 22,
}

commands = ['interface loopback0',
            'ip address 192.168.252.1 255.255.255.255'
            'exit',
            'interface fa0/1',
            'speed 100',
            'full-duplex',
            'no shutdown',
            'exit',
            'router ospf 1',
            'network 10.0.0.0 0.255.255.255 area 0',
            'network 192.168.100.0 0.0.0.255 area 1',
            'exit',
            'router bgp 64512',
            'neighbor 192.168.252.2 remote-as 64512']


ssh = netmiko.ConnectHandler(**cisco_router)
# result = ssh.send_command("show ip inter bri")
# print(result)
res = ssh.send_config_set(commands)
print(res)