import sqlite3
from sqlite3 import OperationalError

def dump_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    fd = open('insert.sql', 'r')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')

    for command in sqlCommands:
        try:
            c.execute(command)
        except OperationalError as msg:
            print("Command skipped: ", msg, command)

    c.close()
    conn.close()

if __name__ == '__main__':
    dump_db()