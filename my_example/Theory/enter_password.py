import getpass
import pexpect
import telnetlib
from time import sleep

# passwd = getpass.getpass()
# print(passwd)

# ssh = pexpect.spawn("ssh cisco@192.168.177.167")
# res = ssh.expect('[Pp]assword')
# print(res)

with telnetlib.Telnet("192.168.177.167") as tn:
    tn.read_until(b"Username:", 5)
    sleep(1)
    tn.write(b"cisco\n")
    sleep(1)
    tn.read_until(b"Password:", 5)
    sleep(1)
    tn.write(b"cisco\n")
    sleep(1)
    index, match, out = tn.expect([b"[>#]"])
    if ">" in match.group().decode("ascii"):
        sleep(1)
        tn.write(b"enable\n")
        sleep(1)
        tn.read_until(b"Password:")
        sleep(1)
        tn.write(b"cisco\n")
        sleep(1)
        sleep(1)
        tn.write(b"show ip inter bri\n")
        sleep(1)
        tn.write(b"show arp\n")
        sleep(1)
        res = tn.read_very_eager().decode("utf-8")
        sleep(1)
        tn.write(b"exit\n")
        sleep(1)
        tn.write(b"exit\n")
        print(res)