import sqlite3
from sqlite3 import Error


def create_engine(db_file):
    #print(db_file)
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


if __name__ == '__main__':
    create_engine('temp.db')