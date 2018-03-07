#!/usr/bin/env python3

from collections import OrderedDict
import datetime

from peewee import *

db = SqliteDatabase('journal.db')

class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta():
        database = db

def initialize():
    """Create db and table if they don't exist"""
    db.connect()
    db.create_tables([Entry], safe=True)

def menu_loop():
    """Show the Menu"""
    choice = None

    while choice != 'q':
        print("Enter 'q' to quit")
        for key, value in menu.items():
            print(f'{key}) {value.__doc__}')
        choice = input('Action: ').lower().strip()

        if choice in menu:
            menu[choice]()
        else:
            continue

def add_entry():
    """Create New Entry"""
    entry = input("Write your entry here: ")

    Entry.create(content=entry)

def view_entries():
    """View all entries"""
    entries = Entry.select()
    for entry in entries:
        print(entry.content)

def delete_entry(entry):
    """Delete an Entry"""

menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries)
])

if __name__ == '__main__':
    initialize()
    menu_loop()
