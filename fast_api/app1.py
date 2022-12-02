import fastapi
import database
import pydantic_models
import config

# Для запуска: uvicorn app:api --reload

api = fastapi.FastAPI()

response = {"Ответ":"Который возвращает сервер"}

@api.get('/')
def index():
    return response

@api.get('/hello')
# http://127.0.0.1:8000/hello
def hello():
    return "hello"

@api.get('/about/us')
#http://127.0.0.1:8000/about/us
def about():
    return {"We Are":"Legion"}