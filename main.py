# Author: August Frisk
# GitHub username: @4N0NYM0U5MY7H
# Date: 2023, January 21
# Description:

import sys
import sqlite3
import re
from contextlib import closing
from UserInterace import MainMenu, AddRecordMenu


def initiate_database():
    """Creates a sqlite3 database if it does not exist."""
    with closing(sqlite3.connect("book_log.db")) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS books (book_id INTEGER PRIMARY KEY,
            title VARCHAR(200) NOT NULL,
            author VARCHAR(100) NOT NULL,
            date VARCHAR(10))""")


def add_record():
    """Adds a new record to the database."""
    book_title = prompt_book_title()
    author_name = prompt_book_author()
    date_completed = prompt_date_completed()

    with closing(sqlite3.connect("book_log.db")) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("""INSERT INTO books(title, author, date)
            VALUES (?,?,?)""", (book_title, author_name, date_completed))
        connection.commit()

    success_string = f"{book_title} by {author_name} completed on {date_completed}."
    print(f"Book successfully added!\n{success_string}")


def prompt_book_title():
    """Prompt the user to enter the title of a book."""
    while True:
        print("Enter a Book Title.\n" +
              "Must only use A(a)-Z(z). Can include spaces.\n" +
              "Must be less than 200 characters.")
        book_title = input("Book Title: ")
        if re.search("^[a-zA-Z\s]+$", book_title):
            if len(book_title) < 201:
                break
    return book_title


def prompt_book_author():
    """Prompt the user to enter the author of a book."""
    while True:
        print("Enter an Author's name.\n" +
              "Must only use A(a)-Z(z). Can include spaces.\n" +
              "Must be less than 100 characters.")
        author_name = input("Author Name: ")
        if re.search("^[a-zA-Z\s]+$", author_name):
            if len(author_name) < 100:
                break
    return author_name


def prompt_date_completed():
    """Prompt the user to enter the date a book was completed."""
    while True:
        print("Enter a date the book was completed.\n"
              + "Must be in the following format: MM/DD/YYYY.")
        date_completed = input("Book Title: ")
        if re.match("(\d{2})[/.-](\d{2})[/.-](\d{4})$", date_completed):
            break
    return date_completed


def remove_record():
    """Removes a record from the database."""
    print("handling remove record...")


def browse_records():
    """Displays all records in the database."""
    print("Displaying all records...")
    print("Book ID | Title | Author Name | Date Completed")
    with closing(sqlite3.connect("book_log.db")) as connection:
        with closing(connection.cursor()) as cursor:
            results = cursor.execute("SELECT * FROM books ORDER BY title DESC").fetchall()
            for row in results:
                print(row)


def exit_program():
    """Exits the program."""
    print("Exiting program...")
    return sys.exit()


if __name__ == "__main__":

    program_title = "CS 361 Book Log"
    program_subtitle = "Tracking your reading since 2023"
    initiate_database()
    main_menu = MainMenu()
    add_record_menu = AddRecordMenu()

    #cursor.execute("CREATE TABLE IF NOT EXISTS books (title TEXT, author TEXT, date TEXT)")
    #rows = cursor.execute("SELECT title, author, date FROM books").fetchall()
    #print(rows)

    print(f"Welcome to the {program_title}!\n{program_subtitle}.")
    while True:
        print(main_menu.display())
        print("Input a number and press ENTER to select an option.")
        while True:
            try:
                selection = int(input("Your input: "))
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
