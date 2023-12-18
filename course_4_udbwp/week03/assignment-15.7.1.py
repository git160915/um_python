import xml.etree.ElementTree as ET
import sqlite3
from sqlite3 import Error

def lookup(element_tree, key):
    key_found = False

    for element in element_tree:
        if key_found: return element.text
        if (element.tag == "key" and element.text == key):
            key_found = True

    return None

conn = sqlite3.connect("assignment-15.7.1.sqlite")
cursor = conn.cursor()

cursor.executescript('''
    DROP TABLE IF EXISTS Track;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Genre;
    DROP TABLE IF EXISTS Artist;
''')

cursor.executescript('''
    CREATE TABLE Artist (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );

    CREATE TABLE Genre (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );

    CREATE TABLE Album (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id  INTEGER,
        title   TEXT UNIQUE
    );

    CREATE TABLE Track (
        id  INTEGER NOT NULL PRIMARY KEY 
            AUTOINCREMENT UNIQUE,
        title TEXT  UNIQUE,
        album_id  INTEGER,
        genre_id  INTEGER,
        len INTEGER, rating INTEGER, count INTEGER
    );
''')

fname = input("Enter file name: ")
if (len(fname) < 1) : fname = "Library.xml"

music_lib = ET.parse(fname)
music_dict = music_lib.findall("dict/dict/dict")
print("Dict count:", len(music_dict))

for entry in music_dict:
    if (lookup(entry, "Track ID") is None): continue

    name = lookup(entry, "Name")
    artist = lookup(entry, "Artist")
    album = lookup(entry, "Album")
    genre = lookup(entry, "Genre")
    count = lookup(entry, "Play Count")
    rating = lookup(entry, "Rating")
    length = lookup(entry, "Rating") 

    if (name is None) or (artist is None) or (album is None) or (genre is None):
        continue

    print(name, artist, album, genre, length, rating, count)

    # INSERT artist into Artist table
    cursor.execute('''
        INSERT OR IGNORE INTO Artist (name) VALUES ( ? )''', (artist,))
    cursor.execute('SELECT id FROM Artist WHERE name = ? ', (artist,))
    artist_id = cursor.fetchone()[0]

    # INSERT album information into Album table
    cursor.execute('''
        INSERT OR IGNORE INTO Album (artist_id, title) VALUES ( ?, ? )''', (artist_id, album))
    cursor.execute('SELECT id FROM Album WHERE title = ? ', (album,))
    album_id = cursor.fetchone()[0]

    # INSERT genre into Genre table
    cursor.execute('''
        INSERT OR IGNORE INTO Genre (name) VALUES ( ? )''', (genre,))
    cursor.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
    genre_id = cursor.fetchone()[0]

    # INSERT genre into Genre table
    cursor.execute('''
        INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count)
        VALUES ( ?, ?, ?, ?, ?, ? )''', (name, album_id, genre_id, length, rating, count))

    try:
        conn.commit()
    except Error as e:
        print(e)
        quit()

print("")
print("====================")
print("")
print("Processing of library,", fname, ", completed SUCCESSFULLY!")