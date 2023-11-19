ip_list = ["10.1.1.1", "10.1.10.1", "10.1.2.1", "10.1.11.1"]


def bin_ip(ip):
    lst = [int(i) for i in ip.split(".")]
    return ("{:08b}"*4).format(*lst)

print(bin_ip("10.1.1.1"))