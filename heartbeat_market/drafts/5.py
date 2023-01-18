import sqlite3
import datetime as dt

def return_last_entries() -> list:
    conn = sqlite3.connect('usd_spread.sqlite')
    cursor = conn.cursor()
    sql_query = """SELECT  * FROM spread where cur_date = ?"""
    cursor.execute(sql_query, (dt.date.today(),))
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return f'На {res[0][3]} курс покупки: {res[0][0]} руб за $, курс продажи: {res[0][1]}, спред: {res[0][2]}'
    # return res

print(return_last_entries())