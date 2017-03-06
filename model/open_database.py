import sqlite3
from sqlite3 import OperationalError
import os


def load_database():
    """
    Its a function to remove database if its existing and create a new one using a script in sql format

    """
    # try:
    #     os.remove('baza_danych.db') # it was said that deleting database every time we open a file is not proper
    # except OSError:
    #     pass

    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()

    # Open and read the file as a single buffer
    fd = open('model/user_database.sql', 'r')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')

    # Execute every command from the input file
    for command in sqlCommands:
        try:
            c.execute(command)
        except OperationalError as msg:
            print("Command skipped: ", msg, command)

    c.close()
    conn.close()