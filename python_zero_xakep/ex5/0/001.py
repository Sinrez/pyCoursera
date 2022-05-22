# import requests
# response = requests.head('https://ya.ru')
# print(response)

def check_url(url_ping):
    if 'http' not in url_ping[:5]:
        url_ping = 'http://'+ url_ping
    if 'https' not in url_ping[:5]:
        url_ping = 'https://' + url_ping
    # if 'http://www.' not in url_ping[:11]:
    #     url_ping = 'http://www.' + url_ping
    # if 'https//www.' not in url_ping[:11]:
    #     url_ping = 'https//www.' + url_ping
    print(url_ping)

w = input('адрес: ')
check_url(w)

# print(len('http://www')) 10 https://yandex.ru/

# url_ping = 'https://yandex.ru/'
# print(url_ping[:5]) #https://yan

