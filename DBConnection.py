import sqlite3


def create_tables():
    """Creates tables one time from SQL script"""
    global sqlite_connection
    global cursor
    try:
        sqlite_connection = sqlite3.connect('ict4370.db')
        cursor = sqlite_connection.cursor()
        print('Database connection is successful')
        with open('sqlite_tables.sql', 'r') as sqlite_file:
            sql_script = sqlite_file.read()
        cursor.executescript(sql_script)
        print("SQLite script executed successfully")
        cursor.close()
    except Exception as e:
        print('Connection to Database has failed due to:', e)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("The SQLite connection is closed")


def db_connection():
    """This function creates the sql connection with the db"""
    global sqlite_connection
    global cursor
    try:
        sqlite_connection = sqlite3.connect('ict4370.db')
        cursor = sqlite_connection.cursor()
    except Exception as e:
        print('Connection to Database has failed due to:', e)
    return sqlite_connection, cursor


def db_execution():
    """This function executes the sql query"""
    try:
        sqlite_connection.commit()
        cursor.close()
    except Exception as e:
        print('Connection to Database has failed due to:', e)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
