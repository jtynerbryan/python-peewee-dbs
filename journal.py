#!/usr/bin/env python3

from collections import OrderedDict
import datetime
import sys

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
    print("Enter your entry. press ctrl+d when finished")
    data = sys.stdin.read().strip()

    if data:
        if input(" Save entry? y/n ").lower() != 'n':
            Entry.create(content=data)
            print("Saved successfully!")

def view_entries(search_query=None):
    """View all entries"""
    entries = Entry.select().order_by(Entry.timestamp.desc())
    if search_query:
        entries = entries.where(Entry.content.contains(search_query))
    for entry in entries:
        timestamp = entry.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        print(f"\n{timestamp}\n{'='*len(timestamp)} \n{entry.content}")
        user_response = input("\nPress 'N' for next entry, 'd' delete entry, 'q' return to Main Menu (N/q) ").lower().strip()
        if  user_response == 'q':
            return
        elif user_response == 'd':
            if input("Are you sure? y/n ").lower() == 'y':
                delete_entry(entry)
        else:
            continue

def search_entries():
    """Search entries for a string"""
    view_entries(input('Search query: '))


def delete_entry(entry):
    """Delete an Entry"""
    entry.delete_instance()
    print("Entry successfully deleted")

menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries),
])

if __name__ == '__main__':
    initialize()
    menu_loop()
