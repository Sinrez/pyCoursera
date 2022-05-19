import subprocess

# Ещё один способ перехватить вывод запущенной сторонней программы

def ping_ip(ip_address):

    print('Проверяю IP: ' + ip_address)
    
    reply = subprocess.run(['ping', ip_address],
                           stdout=subprocess.PIPE, 
                           stderr=subprocess.PIPE,
                           encoding='cp866',
                           shell=True)
    
    if reply.returncode == 0:
        return reply.stdout
    else:
        return 'Произошла ошибка!'
    print('-----------------------------')

print(ping_ip('8.8.8.8'))
print(ping_ip('127.0.0.1'))
