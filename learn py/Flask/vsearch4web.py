from flask import Flask, render_template, request
from vl2 import search4letters

app = Flask(__name__)

@app.route('/search4', methods=['POST'])
def do_search() ->str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    title = 'Here are your results:» (Ваши результаты: )'
    log_request(request, results)
    return render_template('results.html', the_phrase = phrase, the_letters = letters, the_results = results, the_title = title,)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',the_title='Welcome to search4letters on the web!')

def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearh.log','a') as log:
        print(req, res, file =log)

if __name__ =='__main__':
    app.run(debug=True)