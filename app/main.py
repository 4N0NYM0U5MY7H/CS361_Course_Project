# Author: August Frisk
# GitHub username: @4N0NYM0U5MY7H
# Date: 2023, February 24
# Description: The main driver program for the CS 361 Book Log program.

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
from utility import (
    exit_program,
    continue_to_main_menu,
    prompt_for_viewport,
    view_in_console,
    wait_for_microservice_response,
    MicroserviceException,
    write_to_file,
)


__version__ = "1.4.4"


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


if __name__ == "__main__":

    program_title = "CS361 Book Log"
    program_subtitle = "Tracking your reading since 2023"

    os.makedirs("data/", exist_ok=True)
    path_to_txt_file = "data/request.txt"
    path_to_json_file = "data/books.json"
    path_to_html_file = "data/response.html"
    book_database = BookDatabase()

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

            # VIEW RESULTS IN CONSOLE
            if viewport_selction == "NO":
                view_in_console(search_results)
                continue_to_main_menu()
                continue

            # VIEW RESULTS IN BROWSER
            if viewport_selction == "YES":
                search_results = book_database.generate_json_data()
                json_string = json.dumps(search_results)
                write_to_file(json_string, path_to_json_file)
                write_to_file("request", path_to_txt_file)
                try:
                    wait_for_microservice_response(path_to_html_file)
                except MicroserviceException as error:
                    print(error)
                    continue_to_main_menu()
                    continue
                else:
                    webbrowser.open("file://" + os.path.realpath(path_to_html_file))
                    continue_to_main_menu()
                    continue

        # VIEW ALL RECORDS
        elif main_menu_selection == valid_main_menu_options[2]:

            viewport_selection = prompt_for_viewport()

            # VIEW RESULTS IN CONSOLE
            if viewport_selection == "NO":
                view_in_console(book_database.view_all_entries())
                continue_to_main_menu()
                continue

            # VIEW RESULTS IN BROWSER
            if viewport_selection == "YES":
                book_database.view_all_entries()
                search_results = book_database.generate_json_data()
                json_string = json.dumps(search_results)
                write_to_file(json_string, path_to_json_file)
                write_to_file("request", path_to_txt_file)
                try:
                    wait_for_microservice_response(path_to_html_file)
                except MicroserviceException as error:
                    print(error)
                    continue_to_main_menu()
                    continue
                else:
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
            write_to_file("exit", path_to_txt_file)
            exit_program()
