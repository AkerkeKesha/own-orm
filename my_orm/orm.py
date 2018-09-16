from sqlite3 import Error
from engine import create_engine


def create_table(conn, create_table_query):
    try:
        c = conn.cursor()
        c.execute(create_table_query)
    except Error as e:
        print(e)


def main():
    conn = create_engine('temp.db')
    if conn is not None:
        #create_table_query = Query()
        create_table(conn, 'CREATE TABLE ;')
    else:
        print("Error: cannot create db. ")


if __name__ == '__main__':
    main()

# class Base:
#     __tablename__ = ''
#     id = None
#     field_names = None
#     connection = None
#
#     def __init__(self, id, field_names, connection):
#         pass
#
#     def select_all(self):
#         #field_names = [k for k in self.__class__.__dict__.keys() if not k.startswith('__')]
#         #print('SELECT %s FROM %s;' % (', '.join(field_names), self.__class__.__tablename__))
#         pass
