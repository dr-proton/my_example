import paramiko
from time import sleep
import yaml

def send_show_command(arg1, arg2):
    max_byte = 60000
    try:
        cl = paramiko.SSHClient()
        cl.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        cl.connect(hostname=arg1["ip"], 
                username=arg1["user"], 
                password=arg1["passwd"], 
                look_for_keys=False,
                allow_agent=False)
    
    
        with cl.invoke_shell() as ssh:
            # ssh.send('enable\n')
            # sleep(1)
            # ssh.send(f'{arg1["enable"]}\n')
            for command in arg2:
                ssh.send(command + "\n")
                ssh.settimeout(arg1["timeout"])
                sleep(1)

            res = ssh.recv(max_byte)

        return res
    
    except TimeoutError:
        print("Не удалось подключиться к устройству!")
    except paramiko.ssh_exception.AuthenticationException:
        print("Неверный логин или пароль!")



if __name__ == "__main__":
    with open("devices.yaml") as file:
        res = yaml.safe_load(file)

    lst_command = ["sh clock", "sh arp"]
    dct_auth = {"ip": "192.168.177.171", "user": "cisco", "passwd": "cisco", "enable": "cisco", "timeout": 10}
    print(send_show_command(dct_auth, lst_command))   