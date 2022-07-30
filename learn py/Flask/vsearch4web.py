from flask import Flask, render_template
from vl2 import search4letters


app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/search4')
def do_search() ->str:
    return str(search4letters('ife, the universe, and everything!', 'eiru,!'))

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',the_title='Welcome to search4letters on the web!')

app.run()