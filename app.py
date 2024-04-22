import datetime as dt
import os
import sqlite3

from dotenv import load_dotenv
from sqlite3 import Error

load_dotenv()


DB_LOCATION="./other-repo/mytest.db"

def sql_connection():
    """ Create a connection with SQLite database specified
        by the mytest.db file
    :param con: the connection object
    :return: connection object or Error"""
    try:
        db = sqlite3.connect(DB_LOCATION)
        return db
    except Error:
        print(Error)


def create_table(con):
    """ Create the table with given columns
    """
    try:
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY,
        name TEXT,
        surname TEXT,
        department TEXT,
        position TEXT,
        salary REAL,
        date TEXT);''')
        con.commit()
        print('The table is created successfully')
    except Error:
        print(Error)

def create_dump_table(con):
    """ Create the table with given columns
    """
    try:
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS logger(
        created_at TEXT,
        message_content TEXT
        ;''')
        con.commit()
        print('The table is created successfully')
    except Error:
        print(Error)

def insert_data(con, entities):
    """  Insert records into the table
    """
    query = """INSERT INTO employees (id, name, surname, department, position,
            salary, date) VALUES(?,?,?,?,?,?,?)"""

    try:
        cur = con.cursor()
        cur.execute(query, entities)
        con.commit()
        print("The record added successfully")
    except Error:
        print(Error)


def add_data(con):
    """ The second method to add records into the table"""
    try:
        cur = con.cursor()
        cur.execute("INSERT INTO employees VALUES(2, 'David', 'Anderson', 'IT', 'Dev', 3000, '2020-06-01')")
        cur.execute("INSERT INTO employees VALUES(3, 'Tom', 'Roger', 'IT', 'Manager', 3000, '2018-03-02')")
        cur.execute("INSERT INTO employees VALUES(4, 'Alan', 'Meyer', 'IT', 'Dev', 5000, '2019-04-15')")
        con.commit()
        print("The records added successfully")
    except Error:
        print(Error)


def select_all(con):
    """Selects all rows from the table to display
    """
    try:
        cur = con.cursor()
        cur.execute('SELECT * FROM employees')
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Error:
        print(Error)


def update_data(con, salary, id):
    """ Update the table with given new values"""
    try:
        cur = con.cursor()
        cur.execute("UPDATE employees SET salary = ?  WHERE id = ?", (salary,
                                                                      id))
        con.commit()
        print("The record updated successfully")
    except Error:
        print(Error)


def delete_record(con, surname):
    """ Delete the given record
    """
    query = "DELETE FROM employees WHERE surname = ?;"
    try:
        cur = con.cursor()
        cur.execute(query, (surname,))
        con.commit()
        print("The record delated successfully")
    except Error:
        print(Error)

def insert_new_data(con, entities):
    """  Insert records into the table
    """
    query = """INSERT INTO logger (created_at, message_content) VALUES(?,?)"""

    try:
        cur = con.cursor()
        cur.execute(query, entities)
        con.commit()
        print("The record added successfully")
    except Error:
        print(Error)


def main():
    con = sql_connection()
    create_table(con)
    entities = (1, 'Anna', 'Smith', 'IT', 'Dev', 2000, '2020-02-09')
    insert_data(con, entities)
    add_data(con)
    select_all(con)
    update_data(con, 3000, 1)
    delete_record(con, "Roger")
    con.close()


if __name__ == "__main__":
    main()
    print(f"\n\n MAIN FUNCTION END \n")
    print(f"GITHUB_RUN_ID = {os.environ.get('GITHUB_RUN_ID')}")
    print(f"GITHUB_SHA: {os.environ.get('GITHUB_SHA')}")
    print(f"GITHUB_EVENT_NAME: {os.environ.get('GITHUB_EVENT_NAME')}")
    print(f"GITHUB_JOB: {os.environ.get('GITHUB_JOB')}")

    print(f"Message: { os.environ.get('GITHUB_EVENT_INPUTS_MESSAGE1') }")
    message_data = os.environ.get('INPUT_MESSAGE')
    print(f"Tags: {message_data}")

    log_data = (dt.datetime.now, message_data)
    insert_new_data(con, log_data)
    print(f"\n\n SCRIPT END \n")