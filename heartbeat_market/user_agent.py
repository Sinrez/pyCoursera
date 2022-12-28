from random import choice

def make_usr_agent():
    while line := open('user_agent.txt').read().split('\n'):
        user_agent = {'user-agent': choice(line)}
        return user_agent

if __name__ == '__main__':
    print(make_usr_agent())
