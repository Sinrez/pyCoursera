import sqlite3

def view_the_log_formdb():
    conn = sqlite3.connect('vsearh_log.sqlite', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM vsearhlog_tb')
    row = cursor.fetchone()
    while row is not None:
        print(row[0])
        print(row[1])
        print(row[2])
        print(row[3])
        print(row[4])
        # print(row[5])
        print('-------------')
        row = cursor.fetchone()

if __name__ =='__main__':
    view_the_log_formdb()