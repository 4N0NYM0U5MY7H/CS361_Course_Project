# Author: August Frisk
# GitHub username: @4N0NYM0U5MY7H
# Date: 2023, February 18
# Description: The main driver program for the CS 361 Book Log program.

import re
import sys
import os
import time
import json
import webbrowser
from UserInterace import UserInterface
from BookDatabase import (
    BookDatabase,
    enter_book_id,
    enter_book_title,
    enter_author_name,
    enter_date_completed,
)


__version__ = "1.4.3"


def exit_program():
    return sys.exit()


def continue_to_main_menu():
    input("Press ENTER to continue...")
    print("Returning to Main Menu...")


def search_records(database=BookDatabase, menu=UserInterface):
    valid_options = list(menu.get_options())
    selection = menu.get_menu_selection()

    if selection == valid_options[0]:
        return database.search(selection, enter_book_title())
    elif selection == valid_options[1]:
        return database.search(selection, enter_author_name())
    elif selection == valid_options[2]:
        return database.search(selection, enter_date_completed())
    elif selection == valid_options[3]:
        return database.view_all_entries()


def prompt_for_viewport():
    print("View results in a web browser?")
    print("Type 'yes' or 'no' and press ENTER to select an option.")
    while True:
        try:
            user_selection = input("Your input: ").upper()
            if re.match("^([yY][eE][sS])|([nN][oO])$", user_selection) is None:
                raise ValueError
        except ValueError:
            print("Only 'yes' or 'no' are accepted")
            continue
        else:
            return user_selection


def view_in_console(search_results):
    print("Displaying records...")
    print("Book ID | Title | Author Name | Date Completed")
    print(search_results)


def wait_for_microservice_response(filename):
    print("Waiting for response from microservice...")
    while True:
        time.sleep(1)
        try:
            with open(filename, "r") as response:
                try:
                    response.readline()
                except OSError as error:
                    print(f"Recieve Response: {error}")
                    continue
        except PermissionError as error:
            print(f"Receive Response: {error}")
            continue
        except FileNotFoundError:
            print("The microservice failed to respond.")
            continue
        else:
            break


def send_microservice_request(data, filename):
    try:
        with open(filename, "w") as out_file:
            try:
                out_file.write(str(data))
            except OSError as error:
                print(f"send_microservice: {error}")
                continue_to_main_menu()
    except PermissionError as error:
        print(f"send_microservice: {error}")
        continue_to_main_menu()


if __name__ == "__main__":

    program_title = "CS361 Book Log"
    program_subtitle = "Tracking your reading since 2023"
    book_database = BookDatabase()

    # microservice communication files
    # waiting for partner to complete microservice
    path_to_txt_file = "../data/books.txt"
    path_to_json_file = "../data/request.json"
    path_to_html_file = "../data/response.html"

    main_menu_options = {
        1: "Add a book to your records",
        2: "Search for a book",
        3: "View all books in your records",
        4: "Remove a book from your records",
        5: "Exit Program",
    }
    main_menu = UserInterface("Main Menu", main_menu_options)

    add_record_menu_options = {
        "Book Title": "Title of the book",
        "Author Name": "First and last name of the author",
        "Date Completed": "Date the book was completed",
    }
    add_record_menu = UserInterface("Add Record", add_record_menu_options)

    search_records_menu_options = {
        1: "Search by title of the book",
        2: "Search by author's name",
        3: "Search by date the book was completed",
        4: "View all entries",
    }
    search_records_menu = UserInterface("Search Records", search_records_menu_options)
    remove_record_menu = UserInterface("Remove Record", search_records_menu_options)

    print(f"Welcome to the {program_title}!\n{program_subtitle}.")
    time.sleep(2)

    valid_main_menu_options = list(main_menu.get_options())

    while True:
        print(main_menu.display())
        main_menu_selection = main_menu.get_menu_selection()

        # ADD NEW RECORD
        if main_menu_selection == valid_main_menu_options[0]:
            print(add_record_menu.display())
            book_data = (
                enter_book_title(),
                enter_author_name(),
                enter_date_completed(),
            )
            book_database.add_new_entry(book_data)
            continue_to_main_menu()
            continue

        # SEARCH RECORDS
        elif main_menu_selection == valid_main_menu_options[1]:
            print(search_records_menu.display())
            search_results = search_records(book_database, search_records_menu)

            if "No results found" in search_results:
                print(search_results)
                continue_to_main_menu()
                continue

            viewport_selction = prompt_for_viewport()

            if viewport_selction == "NO":
                view_in_console(search_results)
                continue_to_main_menu()
                continue

            # VIEW RESULTS IN BROWSER
            if viewport_selction == "YES":
                search_results = book_database.generate_json_data()

                # waiting for partner to complete microservice
                # search_results.update({"status": "request"})

                json_string = json.dumps(search_results)
                send_microservice_request(json_string, path_to_json_file)

                # waiting for partner to complete microservice
                # send_microservice_request("request", path_to_txt_file)

                wait_for_microservice_response(path_to_html_file)
                webbrowser.open("file://" + os.path.realpath(path_to_html_file))
                continue_to_main_menu()
                continue

        # VIEW ALL RECORDS
        elif main_menu_selection == valid_main_menu_options[2]:

            viewport_selection = prompt_for_viewport()

            if viewport_selection == "NO":
                view_in_console(book_database.view_all_entries())
                continue_to_main_menu()
                continue

            # VIEW RESULTS IN BROWSER
            if viewport_selection == "YES":
                book_database.view_all_entries()
                search_results = book_database.generate_json_data()

                # waiting for partner to complete microservice
                # search_results.update({"status": "request"})

                json_string = json.dumps(search_results)
                send_microservice_request(json_string, path_to_json_file)

                # waiting for partner to complete microservice
                # send_microservice_request("request", path_to_txt_file)

                wait_for_microservice_response(path_to_html_file)
                webbrowser.open("file://" + os.path.realpath(path_to_html_file))
                continue_to_main_menu()
                continue

        # DELETE A RECORD
        elif main_menu_selection == valid_main_menu_options[3]:
            print(remove_record_menu.display())
            search_results = search_records(book_database, remove_record_menu)

            if "No results found" in search_results:
                print(search_results)
                continue_to_main_menu()
                continue

            view_in_console(search_results)
            book_database.delete_by_id(enter_book_id())
            continue_to_main_menu()
            continue

        # EXIT PROGRAM
        elif main_menu_selection == valid_main_menu_options[-1]:
            print("Exiting program...")
            exit_program()
