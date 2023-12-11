import netmiko

cisco_router = {
    'device_type': 'cisco_ios',
    'host': '192.168.177.174',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco',
    'port': 22,
}

commands = ['router ospf 1',
            'network 10.0.0.0 0.255.255.255 area 0',
            'network 192.168.100.0 0.0.0.255 area 1']

ssh = netmiko.ConnectHandler(**cisco_router)
# result = ssh.send_command("show ip inter bri")
# print(result)
res = ssh.send_config_set(commands)
print(res)