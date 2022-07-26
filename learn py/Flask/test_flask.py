from flask import Flask
from vl2 import search4letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/search4')
def do_search() ->str:
    return str(search4letters('ife, the universe, and everything!', 'eiru,!'))

app.run()