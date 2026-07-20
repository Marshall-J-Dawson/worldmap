#generating the db
import sqlite3
from datetime import datetime
from zoneinfo import ZoneInfo
import json

with open("config.json") as h:
    config = json.load(h)


connection = None
cursor = None

def initialise_database():
    global connection, cursor

    connection = sqlite3.connect('data.db')

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS locations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        latitude REAL NOT NULL,
        longitude REAL NOT NULL,
        timestamp TEXT NOT NULL,
        battery INTEGER
    )
    """)

    connection.commit()
    print("\nDATABASE INITIALISED\n")



def insert_location(latitude, longitude, timestamp, battery):
    cursor.execute("""
        INSERT INTO locations
        (latitude, longitude, timestamp, battery)
        VALUES(?, ?, ?, ?)
    """,(latitude, longitude, timestamp, battery))
    connection.commit()

def get_locations():

    cursor.execute("""
        SELECT latitude, longitude, timestamp, battery
        FROM locations
    """)

    return cursor.fetchall()

def close_database():
    connection.close()

def convert_time(tst):
    local_time = datetime.fromtimestamp(
        tst,
        tz=ZoneInfo(config["location"])
    )

    return local_time.strftime("%Y-%m-%d %H:%M:%S")


