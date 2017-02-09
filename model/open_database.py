import sqlite3
from sqlite3 import OperationalError
import os

def loading_database():
    try:
        os.remove('baza_danych.db')
    except OSError:
        pass

    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()

    # Open and read the file as a single buffer
    fd = open('baza_danych.sql', 'r')
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

loading_database()