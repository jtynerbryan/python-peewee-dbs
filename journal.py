#!/usr/bin/env python3

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

def add_entry():
    """Create New Entry"""

def view_entries():
    """View all entries"""

def delete_entry(entry):
    """Delete an Entry"""

if __name__ == '__main__':
    initialize()
    menu_loop()
