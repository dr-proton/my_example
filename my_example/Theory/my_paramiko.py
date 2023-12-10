import paramiko
from time import sleep

def ssh_con(ip):
    res = ""
    user = "cisco"
    passwd = "cisco"
    enable = "cisco"
    max_byte = 60000
    cl = paramiko.SSHClient()
    cl.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    cl.connect(hostname=ip, username=user, password=passwd, look_for_keys=False, allow_agent=False)
    with cl.invoke_shell() as ssh:
        ssh.send(f"{passwd}\n")
        sleep(1)
        ssh.send(f"{enable}\n")
        sleep(1)
        ssh.send("show ip int bri\n")
        ssh.settimeout(5)
        sleep(1)
        res = ssh.recv(max_byte)
    return res

if __name__ == "__main__":
    ip = "192.168.177.168"
    res = ssh_con(ip)
    print(res)