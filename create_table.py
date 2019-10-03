from models.user import UserModel
from resources.item import *
from dbconn import Database


with Database(UserModel.DB_NAME) as connection:
    cursor = connection.cursor()

    create_table = 'CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY, username text, password text)'.format(UserModel.TABLE_NAME)
    cursor.execute(create_table)


with Database(Item.DB_NAME) as connection:
    cursor = connection.cursor()

    create_table = 'CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY, name text, price text)'.format(Item.TABLE_NAME)
    cursor.execute(create_table)
