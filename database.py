import sqlite3
from datetime import datetime
from zoneinfo import ZoneInfo
import json
import os

with open("config.json") as h:
    config = json.load(h)


DATABASE = "data.db"


def initialise_database():

    connection = sqlite3.connect(DATABASE)
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
    connection.close()

    print("\nDATABASE INITIALISED\n")


def insert_location(latitude, longitude, timestamp, battery):

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO locations
        (latitude, longitude, timestamp, battery)
        VALUES (?, ?, ?, ?)
    """, (latitude, longitude, timestamp, battery))

    connection.commit()
    connection.close()


def get_locations():

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT latitude, longitude, timestamp, battery
        FROM locations
    """)

    locations = cursor.fetchall()

    connection.close()

    return locations


def convert_time(tst):

    local_time = datetime.fromtimestamp(
        tst,
        tz=ZoneInfo(config["location"])
    )

    return local_time.strftime("%Y-%m-%d %H:%M:%S")

def clear_database():
    if os.path.exists(DATABASE):
        os.remove(DATABASE)
        print("Database file deleted successfully.")
    else:
        print("Database file does not exist.")