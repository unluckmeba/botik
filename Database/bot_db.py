import sqlite3
from config import bot
import random


def sql_create():
    global db, cursor
    db = sqlite3.connect('bot.sqlite3')
    cursor = db.cursor()

    if db:
        print('база данных подключен')
    db.execute(
        "CREATE TABLE IF NOT EXISTS anketa"
        "(id INTEGER PRIMARY KEY, fullname TEXT,"
        "direction TEXT)"
    )
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO anketa VALUES (?,?,?,?,?)", tuple(data.values()))
        db.commit()


async def sql_command_all():
    return cursor.execute('SELECT * FROM anketa').fetchall()


async def sql_command_delete(id):
    cursor.execute("DELETE FROM anketa WHERE id = ?", (id,))
    db.commit()


async def sql_commands_get_all_id():
    return cursor.execute('SELECT id FROM anketa').fetchall()
