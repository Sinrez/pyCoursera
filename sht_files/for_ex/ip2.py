import ipaddress


def has_access(ip, network):
    # Преобразовываем адреса.
    ip = ipaddress.ip_address(ip)
    network = ipaddress.ip_network(network)

    # Выводим данные.
    return True if ip in network.hosts() else False