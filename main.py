# Author: August Frisk
# GitHub username: @4N0NYM0U5MY7H
# Date: 2023, January 21
# Description: The main driver program for the CS 361 Book Log program.

import re
import sys
import time
import json
import webbrowser
from UserInterace import MainMenu, AddRecordMenu, RemoveRecordMenu, SearchRecordsMenu
from BookLogDB import BookLogDB


__version__ = "1.1.0"


def exit_program():
    """Exits the program."""
    return sys.exit()


def continue_to_main_menu():
    """Prompts the user to continue to the Main Menu."""
    input("Press ENTER to continue...")
    print("Returning to Main Menu...")


def search_records(database, menu):
    """Returns search results from the book database."""
    valid_search_options = list(menu.get_options())

    print("Input a number and press ENTER to select an option.")
    while True:
        try:
            search_selection = int(input("Your input: "))
            if (
                re.search(
                    f"[{valid_search_options[0]}-{valid_search_options[-1]}]",
                    str(search_selection),
                )
                is None
            ):
                raise ValueError
        except ValueError:
            print(
                f"Only INTEGER values between {valid_search_options[0]} and {valid_search_options[-1]} accepted!"
            )
            continue
        else:
            break

    # SEARCH BY TITLE
    if search_selection == valid_search_options[0]:
        return database.search_by_title()
    # SEARCH BY AUTHOR
    elif search_selection == valid_search_options[1]:
        return database.search_by_author()
    # SEARCH BY DATE
    elif search_selection == valid_search_options[2]:
        return database.search_by_date()
    # VIEW ALL RECORDS
    elif search_selection == valid_search_options[3]:
        return database.view_all_records()


if __name__ == "__main__":
    """Main driver program for the CS 361 Portfolio Project."""

    program_title = "CS 361 Book Log"
    program_subtitle = "Tracking your reading since 2023"
    book_database = BookLogDB()
    main_menu = MainMenu()
    add_record_menu = AddRecordMenu()
    remove_record_menu = RemoveRecordMenu()
    search_records_menu = SearchRecordsMenu()

    print(f"Welcome to the {program_title}!\n{program_subtitle}.")
    time.sleep(2)

    valid_main_menu_options = list(main_menu.get_options())

    while True:
        print(main_menu.display())
        print("Input a number and press ENTER to select an option.")
        while True:
            try:
                main_menu_input = int(input("Your input: "))
                if (
                    re.search(
                        f"[{valid_main_menu_options[0]}-{valid_main_menu_options[-1]}]",
                        str(main_menu_input),
                    )
                    is None
                ):
                    raise ValueError
            except ValueError:
                print(
                    f"Only INTEGERS from {valid_main_menu_options[0]} to {valid_main_menu_options[-1]} are accepted!"
                )
                continue
            else:
                break

        # ADD NEW RECORD
        if main_menu_input == valid_main_menu_options[0]:
            print(add_record_menu.display())
            book_database.add_new_record()
            continue_to_main_menu()
            continue

        # SEARCH RECORDS
        elif main_menu_input == valid_main_menu_options[1]:
            print(search_records_menu.display())
            search_results = search_records(book_database, search_records_menu)

            if "No results found" in search_results:
                print(search_results)
                continue_to_main_menu()
                continue

            # PROMPT FOR WEB VIEW
            print("View results in a web browser?")
            print("Type 'yes' or 'no' and press ENTER to select an option.")
            while True:
                try:
                    browser_view_input = input("Your input: ").upper()
                    if (
                        re.search("^([yY][eE][sS])|([nN][oO])$", browser_view_input)
                        is None
                    ):
                        raise ValueError
                except ValueError:
                    print("Only 'yes' or 'no' are accepted")
                    continue
                else:
                    break

            # VIEW RESULTS IN CONSOLE
            if browser_view_input == "NO":
                print("Displaying records...")
                print("Book ID | Title | Author Name | Date Completed")
                print(search_results)
                continue_to_main_menu()
                continue

            # VIEW RESULTS IN BROWSER
            if browser_view_input == "YES":
                # TO DO
                # cast search_results to JSON
                # wait for response from partner's microservice
                # open generated webpage
                continue

        # VIEW ALL RECORDS
        elif main_menu_input == valid_main_menu_options[2]:

            # PROMPT FOR WEB VIEW
            print("View results in a web browser?")
            print("Type 'yes' or 'no' and press ENTER to select an option.")
            while True:
                try:
                    browser_view_input = input("Your input: ").upper()
                    if (
                        re.search("^([Yy][Ee][Ss])|([Nn][Oo])$", browser_view_input)
                        is None
                    ):
                        raise ValueError
                except ValueError:
                    print("Only 'yes' or 'no' are accepted")
                    continue
                else:
                    break

            # VIEW RESULTS IN CONSOLE
            if browser_view_input == "NO":
                print("Displaying records...")
                print("Book ID | Title | Author Name | Date Completed")
                print(book_database.view_all_records())
                continue_to_main_menu()
                continue

            # VIEW RESULTS IN BROWSER
            if browser_view_input == "YES":
                # TO DO
                # cast search_results to JSON
                # wait for response from partner's microservice
                # open generated webpage
                continue

            # DELETE A RECORD
        elif main_menu_input == valid_main_menu_options[3]:
            print(remove_record_menu.display())
            search_results = search_records(book_database, remove_record_menu)

            if "No results found" in search_results:
                print(search_results)
                continue_to_main_menu()
                continue
            print("Displaying records...")
            print("Book ID | Title | Author Name | Date Completed")
            print(search_results)
            book_database.delete_a_record()
            continue_to_main_menu()
            continue

        # EXIT PROGRAM
        elif main_menu_input == valid_main_menu_options[-1]:
            print("Exiting program...")
            exit_program()
