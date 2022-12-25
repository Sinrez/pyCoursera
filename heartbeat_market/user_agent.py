import requests
from random import choice



url = 'http://httpbin.org/user-agent'

def make_usr_agent():
    while line := open('user_agent.txt').read().split('\n'):
        user_agent = {'user-agent': choice(line)}
        response = requests.get(url=url, headers=user_agent)
        print(response.text)

if __name__ == '__main__':
    make_usr_agent()