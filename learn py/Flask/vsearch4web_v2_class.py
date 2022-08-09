from flask import Flask, render_template, request, escape, session
from vl2 import search4letters
import sqlite3
from checker import check_logged_in
from time import sleep
from DBcm import UseDatabase, ConnectionError, CredentialsError, SQLError

app = Flask(__name__)
app.secret_key = 'SuperSerucr007pwsd'


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in.'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are logged out'


def add_logs_db(req: 'flask_request', res: str) -> None:
    with UseDatabase() as cursor:
        try:
            # Создаем таблицу лога
            cursor.execute(
                '''CREATE TABLE IF NOT EXISTS vsearhlog_tb ( phrase text, letters text, ip text, browser_string text, results text )''')
        except sqlite3.ProgrammingError:
            print('Таблица не найдена или уже существует')
        except sqlite3.Warning:
            exit('Ошибка БД')
        except Exception as err:
            print(f'Произошла ошибка {str(err)}')
        mydata = (req.form['phrase'], req.form['letters'], req.remote_addr, req.user_agent.platform, res)
        cursor.execute("INSERT INTO vsearhlog_tb (phrase, letters, ip, browser_string, results) VALUES (?, ?, ?, ?, ?)",
                       mydata)



@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    title = 'Here are your results:» (Ваши результаты: )'
    try:
        log_request(request, results)
    except Exception as err:
        print(f'!!!Произошла ошибка при попытке записи лога!!! {str(err)}')
    add_logs_db(request, results)
    return render_template('results.html', the_phrase=phrase, the_letters=letters, the_results=results,
                           the_title=title, )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


def log_request(req: 'flask_request', res: str) -> None:
    sleep(10)
    with open('vsearh.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':
    contents = []
    with open('vsearh.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html', the_title='View Log', the_row_titles=titles, the_data=contents, )


@app.route('/viewlogdb')
@check_logged_in
def view_the_log_formdb() -> 'html':
    contents = []
    try:
        with UseDatabase() as cursor:
            cursor.execute('SELECT * FROM vsearhlog_tb')
            row = cursor.fetchone()
            while row is not None:
                contents.append([])
                for item in row:
                    contents[-1].append(escape(item))
                row = cursor.fetchone()
            titles = ('Form Data', 'Text', 'Remote_addr', 'User_agent', 'Results')
            return render_template('viewlog.html', the_title='View Log', the_row_titles=titles, the_data=contents, )

    except ConnectionError as err:
        print('Подключена ли БД все норм с доступом? Error:', str(err))
    except CredentialsError as err:
        print('User-id/Password issues. Error:', str(err))
    except SQLError as err:
        print('Все правильно с запросом к БД? Error:', str(err))
    except Exception as err:
        print('Что пошло не так :', str(err))
    return 'Error'

if __name__ == '__main__':
    app.run(debug=True)
