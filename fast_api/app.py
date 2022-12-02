import fastapi
import database
import pydantic_models
import config

api = fastapi.FastAPI()

fake_database = {'users':[

    {
        "id":1,             # тут тип данных - число
        "name":"Anna",      # тут строка
        "nick":"Anny42",    # и тут
        "balance": 15.01    # а тут float
     },

    {
        "id":2,             # у второго пользователя
        "name":"Dima",      # такие же
        "nick":"dimon2319", # типы
        "balance": 8.01     # данных
     }
    ,{
        "id":3,             # у третьего
        "name":"Vladimir",  # юзера
        "nick":"Vova777",   # мы специально сделаем
        "balance": "23"     # нестандартный тип данных в его балансе
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