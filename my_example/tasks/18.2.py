import netmiko
import yaml

def send_config_commands(device, config_commands ):
    for data in device:
        res = ""
        ssh = netmiko.ConnectHandler(**data)
        if not ssh.check_config_mode():
            ssh.config_mode()
            res = ssh.send_config_set(config_commands)
            ssh.exit_config_mode()
            
            ssh.disconnect()
            print(res)
    



if __name__ == "__main__":
    with open("devices.yaml", "r") as file:
        device = yaml.safe_load(file)
        
    commands = ['logging 10.255.255.1', 'logging buffered 20010', 'no logging console']
    # device = {'device_type': 'cisco_ios',
    # 'ip': '192.168.177.161',
    # 'username': 'cisco',
    # 'password': 'cisco',
    # 'secret': 'cisco'}

    send_config_commands(device, commands)
    