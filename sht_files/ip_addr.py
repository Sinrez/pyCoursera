import ipaddress, sys

ip = sys.argv[1]
host_ip = sys.argv[2]

def has_access(ip, host_ip):
    res = False
    ip_1 = ipaddress.ip_address(ip)
    ip_2 = list(ipaddress.ip_network(host_ip).hosts())
    for i in ip_2:
        if i == ip_1:
            res = True
        else:
            pass
    return res