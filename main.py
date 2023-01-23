# Author: August Frisk
# GitHub username: @4N0NYM0U5MY7H
# Date: 2023, January 21
# Description:

import sys
import sqlite3
import re
from contextlib import closing
from UserInterace import MainMenu, AddRecordMenu, RemoveRecordMenu


def initiate_database():
    """Creates a sqlite3 database if it does not exist."""
    with closing(sqlite3.connect("book_log.db")) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("""CREATE TABLE IF NOT EXISTS books (
            book_id INTEGER PRIMARY KEY,
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


def search_by_title():
    """Search for a record by Book Title."""
    book_title = prompt_book_title()
    with closing(sqlite3.connect("book_log.db")) as connection:
        with closing(connection.cursor()) as cursor:
            query = cursor.execute("""SELECT * FROM books WHERE title = ?""", (book_title,)).fetchall()
            results = ""
            if query:
                for row in query:
                    results += f"{row}\n"
                return results
            else:
                return f"No results found with the Book Title {book_title}"


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


def search_by_author():
    """Search for a record by Author Name."""
    author_name = prompt_book_author()
    with closing(sqlite3.connect("book_log.db")) as connection:
        with closing(connection.cursor()) as cursor:
            query = cursor.execute("""SELECT * FROM books WHERE author = ?""", (author_name,)).fetchall()
            results = ""
            if query:
                for row in query:
                    results += f"{row}\n"
                return results
            else:
                return f"No results found with the Author Name {author_name}"


def prompt_date_completed():
    """Prompt the user to enter the date a book was completed."""
    while True:
        print("Enter a date the book was completed.\n"
              + "Must be in the following format: MM/DD/YYYY.")
        date_completed = input("Book Title: ")
        if re.match("(\d{2})[/.-](\d{2})[/.-](\d{4})$", date_completed):
            break
    return date_completed


def search_by_date():
    """Search for a record by Author Name."""
    date_completed = prompt_date_completed()
    with closing(sqlite3.connect("book_log.db")) as connection:
        with closing(connection.cursor()) as cursor:
            query = cursor.execute("""SELECT * FROM books WHERE date = ?""", (date_completed,)).fetchall()
            results = ""
            if query:
                for row in query:
                    results += f"{row}\n"
                return results
            else:
                return f"No results found with the Completion Date {date_completed}"


def remove_record(query_results):
    """Removes a record from the database."""
    if "No results found" in query_results:
        print(query_results)
        return

    print("Displaying records...")
    print("Book ID | Title | Author Name | Date Completed")
    print(query_results)
    print("Enter a Book ID to delete.")
    print("Input a number and press ENTER to select an option.")
    while True:
        try:
            selection = int(input("Your input: "))
        except ValueError:
            continue
        else:
            break
    with closing(sqlite3.connect("book_log.db")) as connection:
        with closing(connection.cursor()) as cursor:
            query = cursor.execute("""SELECT * FROM books WHERE book_id = ?""", (selection,))
            if query.fetchone():
                cursor.execute("DELETE FROM books WHERE book_id = ?", (selection,))
                print(f"Book successfully deleted!")
                connection.commit()
            else:
                print(f"No records found with Book ID {selection}.")


def browse_records():
    """Displays all records in the database."""
    print("Displaying all records...")
    print("Book ID | Title | Author Name | Date Completed")
    with closing(sqlite3.connect("book_log.db")) as connection:
        with closing(connection.cursor()) as cursor:
            query = cursor.execute("SELECT * FROM books ORDER BY title DESC").fetchall()
            results = ""
            for row in query:
                results += f"{row}\n"
    return results


def exit_program():
    """Exits the program."""
    return sys.exit()


if __name__ == "__main__":
    """Main driver program for the CS 361 Portfolio Project."""

    program_title = "CS 361 Book Log"
    program_subtitle = "Tracking your reading since 2023"
    initiate_database()
    main_menu = MainMenu()
    add_record_menu = AddRecordMenu()
    remove_record_menu = RemoveRecordMenu()

    print(f"Welcome to the {program_title}!\n{program_subtitle}.")
    while True:
        print(main_menu.display())
        print("Input a number and press ENTER to select an option.")
        while True:
            try:
                main_menu_selection = int(input("Your input: "))
            except ValueError:
                print(f"Only INTEGER values between 1 and 4 accepted")
                continue
            else:
                break

        if main_menu_selection == list(main_menu.get_options())[0]:
            print(add_record_menu.display())
            add_record()
            print("Returning to Main Menu...")
            continue

        elif main_menu_selection == list(main_menu.get_options())[1]:
            print(remove_record_menu.display())
            print("Input a number and press ENTER to select an option.")
            while True:
                try:
                    remove_record_menu_selection = int(input("Your input: "))
                except ValueError:
                    print(f"Only INTEGER values between 1 and 4 accepted")
                    continue
                else:
                    break

            if remove_record_menu_selection == list(remove_record_menu.get_options())[0]:
                remove_record(search_by_title())
                print("Returning to Main Menu...")
                continue
            elif remove_record_menu_selection == list(remove_record_menu.get_options())[1]:
                remove_record(search_by_author())
                print("Returning to Main Menu...")
                continue
            elif remove_record_menu_selection == list(remove_record_menu.get_options())[2]:
                remove_record(search_by_date())
                print("Returning to Main Menu...")
                continue
            elif remove_record_menu_selection == list(remove_record_menu.get_options())[3]:
                remove_record(browse_records())
                print("Returning to Main Menu...")
                continue
            else:
                print("An unknown error occurred...")

        elif main_menu_selection == list(main_menu.get_options())[2]:
            print(browse_records())
            print("Returning to Main Menu...")
            continue
        elif main_menu_selection == list(main_menu.get_options())[3]:
            print("Exiting program...")
            exit_program()
        else:
            print("something went wrong")
        break
