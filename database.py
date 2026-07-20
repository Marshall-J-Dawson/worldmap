#generating the db
import sqlite3

#define connection to db

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

#save changes
connection.commit()

#close db
connection.close()

print("database created succesfully")