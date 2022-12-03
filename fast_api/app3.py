import fastapi
import database
import pydantic_models
import config
from fastapi import Request     # позволяет нам перехватывать запрос и получать по нему всю информацию

api = fastapi.FastAPI()

@api.get('/')       # метод для обработки get запросов
@api.post('/')      # метод для обработки post запросов
@api.put('/')       # метод для обработки put запросов
@api.delete('/')    # метод для обработки delete запросов
def index(request: Request):  # тут request - будет объектом в котором хранится вся информация о запросе
    return {"Request" : [request.method,    # тут наш API вернет клиенту метод, с которым этот запрос был совершен
                         request.headers]}  # а тут в ответ вернутся все хедеры клиентского запроса

fake_database = {'users':[

    {
        "id":1,             # тут тип данных - число
        "name":"Anna",      # тут строка
        "nick":"Anny42",    # и тут
        "balance": 15300    # а тут float
     },

    {
        "id":2,             # у второго пользователя
        "name":"Dima",      # такие же
        "nick":"dimon2319", # типы
        "balance": 160.23     # данных
     }
    ,{
        "id":3,             # у третьего
        "name":"Vladimir",  # юзера
        "nick":"Vova777",   # мы специально сделаем
        "balance": "25000"     # нестандартный тип данных в его балансе
     }
],}

@api.get('/get_info_by_user_id/{id:int}')
def get_info_about_user(id):
    return fake_database['users'][id-1]

@api.get('/get_user_balance_by_id/{id:int}')
def get_user_balance(id):
    return fake_database['users'][id-1]['balance']


@api.get('/get_total_balance')
def get_total_balance():
    total_balance: float = 0.0
    for user in fake_database['users']:
        total_balance += pydantic_models.User(**user).balance
    return total_balance

@api.get("/users/")
def get_users(skip: int = 0, limit: int = 10):
    # параметры функции подставляются в парамтеры url http://127.0.0.1:8000/users/?skip=1&limit=10
    return fake_database['users'][skip: skip + limit]

@api.get("/user/{user_id}")
def read_user(user_id: str, query: str or None = None):
    """
    Тут значение по умолчанию для query будет None
    """
    if query:
        return {"user_id": user_id, "query": query}
    return {"user_id": user_id}