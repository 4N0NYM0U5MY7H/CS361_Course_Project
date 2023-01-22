# Author: August Frisk
# GitHub username: @4N0NYM0U5MY7H
# Date: 2023, January 21
# Description:

import sys
import sqlite3
from contextlib import closing

def main_menu_options():
    menu_options = {
        1: 'Add a book to your records',
        2: 'Remove a book from your records',
        3: 'View all books in your records',
        4: 'Exit Program'
    }
    return menu_options

def main_menu_text():
    """Displays the Main Menu and options."""
    header = "Main Menu -- Please select an Option"
    separator = '-'
    line = f"{separator * (len(header) + 2)}"
    menu_string = f"{line}\n{header}\n{line}\n"

    for key in main_menu_options().keys():
        menu_string += f"{key} --- {main_menu_options()[key]}\n"

    return menu_string

def add_record(cursor):
    """Adds a new record to the database."""

    print("handling add record...")

def remove_record(cursor):
    """Removes a record from the database."""
    print("handling remove record...")

def browse_records(cursor):
    """Displays all records in the database."""
    print("handling view records...")

def exit_program():
    """Exits the program."""
    print("Exiting program...")
    return sys.exit()


if __name__ == "__main__":

    program_title = "CS 361 Book Log"
    program_subtitle = "Tracking your reading since 2023."
    # sqlite3 database
    connection = sqlite3.connect("book_log.db")
    cursor = connection.cursor()

    #cursor.execute("CREATE TABLE IF NOT EXISTS books (title TEXT, author TEXT, isbn NUMBER, date TEXT)")
    #rows = cursor.execute("SELECT title, author, date FROM books").fetchall()
    #print(rows)

    print(f"{program_title}\n{program_subtitle}")
    while True:
        print(main_menu_text())
        while True:
            try:
                selection = int(input("select an option: "))
            except ValueError:
                valid_options = ""
                for key in main_menu_options().keys():
                    valid_options += f"{key} "
                print(f"Only INTEGER values {valid_options}accepted")
                continue
            else:
                break

        if selection == list(main_menu_options())[0]:
            add_record(cursor)
            break
        elif selection == list(main_menu_options())[1]:
            remove_record(cursor)
            break
        elif selection == list(main_menu_options())[2]:
            browse_records(cursor)
            break
        elif selection == list(main_menu_options())[3]:
            exit_program()
        else:
            print("something went wrong")
        break
