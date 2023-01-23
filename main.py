# Author: August Frisk
# GitHub username: @4N0NYM0U5MY7H
# Date: 2023, January 21
# Description:

import sys
import sqlite3
from contextlib import closing
from UserInterace import MainMenu, AddRecordMenu


def initiate_database():
    """Creates a sqlite3 database if it does not exist."""
    with closing(sqlite3.connect("book_log.db")) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("CREATE TABLE IF NOT EXISTS books "
                           + "(title VARCHAR(255), "
                           + "author VARCHAR(100), "
                           + "date VARCHAR(20))"
                           )


def add_record():
    """Adds a new record to the database."""
    while True:
        try:
            book_title = input("Book Title: ")
        except ValueError:
            print("Not a valid input")
            continue
        else:
            break
    while True:
        try:
            author_name = input("Author Name: ")
        except ValueError:
            print("Not a valid input")
            continue
        else:
            break
    while True:
        try:
            date_completed = input("Date Completed: ")
        except ValueError:
            print("Not a valid input")
            continue
        else:
            break
    test_string = f"{book_title} by {author_name} completed on {date_completed}."
    print(f"{test_string} successful...")


def remove_record():
    """Removes a record from the database."""
    print("handling remove record...")


def browse_records():
    """Displays all records in the database."""
    print("handling view records...")


def exit_program():
    """Exits the program."""
    print("Exiting program...")
    return sys.exit()


if __name__ == "__main__":

    program_title = "CS 361 Book Log"
    program_subtitle = "Tracking your reading since 2023."
    initiate_database()
    main_menu_options = {
        1: 'Add a book to your records',
        2: 'Remove a book from your records',
        3: 'View all books in your records',
        4: 'Exit Program'
    }
    main_menu = MainMenu()
    add_record_menu = AddRecordMenu()

    #cursor.execute("CREATE TABLE IF NOT EXISTS books (title TEXT, author TEXT, date TEXT)")
    #rows = cursor.execute("SELECT title, author, date FROM books").fetchall()
    #print(rows)

    print(f"{program_title}\n{program_subtitle}")
    while True:
        print(main_menu.display())
        while True:
            try:
                selection = int(input("select an option: "))
            except ValueError:
                valid_options = ""
                for valid_key in main_menu.get_options().keys():
                    valid_options += f"{valid_key} "
                print(f"Only INTEGER values {valid_options}accepted")
                continue
            else:
                break

        if selection == list(main_menu.get_options())[0]:
            print(add_record_menu.display())
            add_record()
            break
        elif selection == list(main_menu.get_options())[1]:
            remove_record()
            break
        elif selection == list(main_menu.get_options())[2]:
            browse_records()
            break
        elif selection == list(main_menu.get_options())[3]:
            exit_program()
        else:
            print("something went wrong")
        break
