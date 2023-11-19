from check_ip_function import check_ip

def return_correct_ip(ip_addresses):
    correct = []
    for ip in ip_addresses:
        if check_ip(ip):
            correct.append(ip)
    return correct


print('Проверка списка IP-адресов')
ip_list = ['10.1.1.1', '8.8.8.8', '2.2.2']
correct = return_correct_ip(ip_list)
print(correct)














# import ipaddress


# def check_ip(ip):
#     try:
#         ipaddress.ip_address(ip)
#         return True
#     except ValueError as err:
#         return False


# if __name__ == '__main__':
#     ip1 = '10.1.1.1'
#     ip2 = '10.1.1'

#     print('Проверка IP...')
#     print(ip1, check_ip(ip1))
#     print(ip2, check_ip(ip2))