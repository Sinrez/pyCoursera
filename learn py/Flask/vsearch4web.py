from flask import Flask, render_template, request, escape
from vl2 import search4letters
import sqlite3

app = Flask(__name__)

def add_logs_db(req: 'flask_request', res: str) -> None:
    # Вставляем в таблицу pyblog первую запись со значениями title и article
    conn = sqlite3.connect('vsearh_log.sqlite', check_same_thread=False)
    cursor = conn.cursor()
    try:
        # Создаем таблицу лога
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS vsearhlog_tb ( phrase text, letters text, ip text, browser_string text, results text )''')
    except sqlite3.ProgrammingError:
        print('Таблица не найдена или уже существует')
    except sqlite3.Warning:
        exit('Ошибка БД')
    mydata = (req.form['phrase'], req.form['letters'], req.remote_addr, req.user_agent.browser, res)
    cursor.execute("INSERT INTO vsearhlog_tb (phrase, letters, ip, browser_string, results) VALUES (?, ?, ?, ?, ?)", mydata)
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/search4', methods=['POST'])
def do_search() ->str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    title = 'Here are your results:» (Ваши результаты: )'
    log_request(request, results)
    add_logs_db(request, results)
    return render_template('results.html', the_phrase = phrase, the_letters = letters, the_results = results, the_title = title,)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',the_title='Welcome to search4letters on the web!')

def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearh.log','a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('vsearh.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html', the_title='View Log',the_row_titles=titles, the_data=contents,)

# @app.route('/viewlogdb')
# def view_the_log_formdb():
#     contents = []
#     conn = sqlite3.connect('vsearh_log.sqlite', check_same_thread=False)
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM vsearhlog_tb')
#     row = cursor.fetchone()
#     titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
#     return render_template('viewlog.html', the_title='View Log',the_row_titles=titles, the_data=contents,)
#     # while row is not None:
#     #     print(row[0])
#     #     print(row[1])
#     #     print(row[2])
#     #     print('-------------')
#     #     row = cursor.fetchone()

if __name__ =='__main__':
    app.run(debug=True)
