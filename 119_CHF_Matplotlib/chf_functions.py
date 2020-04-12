""" All functions """

from configparser import ConfigParser
import psycopg2
import sys

f_name = r'D:\Py\118_Currency_quotes\chf_config.ini'


def config(filename=f_name, section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db.setdefault(param[0], param[1])
    else:
        raise Exception(f'Section {section} not found in {f_name}.')
    return db


def connect():
    """ Connects to PostgreSQL """
    try:
        parameters = config()
        connection = psycopg2.connect(**parameters)
        cursor = connection.cursor()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        sys.exit()
    return connection, cursor


def close_connection(connection, cursor):
    if connection:
        cursor.close()
        connection.close()


def select_data(connection, cursor):
    """ SELECT * FROM database """
    try:
        postgres_select_query = """ SELECT * FROM currency_quotes """
        cursor.execute(postgres_select_query)
        records = cursor.fetchall()
        for row in records:
            print(row[1], row[2], row[3], row[4])
    except (Exception, psycopg2.Error) as error:
        if connection:
            print(error)


def select_user_data(connection, cursor, user_data):
    """ SELECT user_data FROM database """
    try:
        user_select_query = f""" SELECT * FROM currency_quotes WHERE date='{user_data}' """
        cursor.execute(user_select_query)
        records = cursor.fetchall()
        for rec in records:
            print(f'{rec[2]}: {rec[3]}, {rec[4]}PLN')
    except (Exception, psycopg2.Error) as error:
        if connection:
            print(error)
