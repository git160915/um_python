import json
import sqlite3

conn = sqlite3.connect("assignment-15.8.1.sqlite")
cursor = conn.cursor()

# Initialise DB with base tables
cursor.executescript('''
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Member;
    DROP TABLE IF EXISTS Course;
                     
    CREATE TABLE User (
        id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );
                     
    CREATE TABLE Course (
        id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title   TEXT UNIQUE
    );
                     
    CREATE TABLE Member (
        user_id     INTEGER,
        course_id   INTEGER,
        role        INTEGER,
        PRIMARY KEY (user_id, course_id)
    );               
''')

fname = input("Enter file name: ")
if (len(fname) < 1): fname = "roster_data.json"

fhandle = open(fname)
roster_string_data = fhandle.read()
roster_json_data = json.loads(roster_string_data)

for entry in roster_json_data:
    user_name = entry[0]
    course_title = entry[1]
    member_role = entry[2]

    print((user_name, course_title, member_role))

    cursor.execute("INSERT OR IGNORE INTO User (name) VALUES ( ? )", (user_name, ))
    cursor.execute("SELECT id FROM User WHERE name = ?", (user_name, ))
    user_id = cursor.fetchone()[0]

    cursor.execute("INSERT OR IGNORE INTO Course (title) VALUES ( ? )", (course_title, ))
    cursor.execute("SELECT id FROM Course WHERE title = ?", (course_title, ))
    course_id = cursor.fetchone()[0]

    cursor.execute('''INSERT OR REPLACE INTO Member (user_id, course_id, role) 
        VALUES (?, ?, ?)''', (user_id, course_id, member_role))

conn.commit()
conn.close()