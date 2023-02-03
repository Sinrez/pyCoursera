from collections import deque

graph ={}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
searched = [] #для уже проверенных, чтобы не было петель-зацикливания

def person_is_seller(name):
    # из постановки задачи - если имя заканчивается на м, то это искомый продавец манго
    return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue += graph['you']

    while search_queue:
        person =  search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(f'{person} - продавец манго!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person) #уже просмотренный
    return False

search("you")