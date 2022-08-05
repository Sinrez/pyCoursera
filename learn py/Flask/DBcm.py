import sqlite3


class ConnectionError(Exception):
    pass


class CredentialsError(Exception):
    pass


class SQLError(Exception):
    pass


class UseDatabase:
    def __init__(self, config: dict):
        self.configuration = config

    def __enter__(self) -> 'cursor':
        try:
            self.conn = sqlite3.connect('vsearh_log.sqlite', check_same_thread=False)
            self.cursor = self.conn.cursor()
            return self.cursor
        except sqlite3.Warning:
            exit('Ошибка БД')
        except Exception as err:
            print(f'Произошла ошибка {str(err)}')

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        if exc_type is sqlite3.Warning:
            raise SQLError(exc_value)
        elif exc_type:
            raise exc_type(exc_value)
