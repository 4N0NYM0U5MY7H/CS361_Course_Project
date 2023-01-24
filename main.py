# Author: August Frisk
# GitHub username: @4N0NYM0U5MY7H
# Date: 2023, January 21
# Description: The main driver program for the CS 361 Book Log program.

import sys
import time
from UserInterace import MainMenu, AddRecordMenu, RemoveRecordMenu
from BookLogDB import BookLogDB


def exit_program():
    """Exits the program."""
    return sys.exit()


def continue_to_main_menu():
    """Prompts the user to continue to the Main Menu."""
    input("Press ENTER to continue...")
    print("Returning to Main Menu...")
    time.sleep(1)


if __name__ == "__main__":
    """Main driver program for the CS 361 Portfolio Project."""

    program_title = "CS 361 Book Log"
    program_subtitle = "Tracking your reading since 2023"
    book_database = BookLogDB()
    main_menu = MainMenu()
    add_record_menu = AddRecordMenu()
    remove_record_menu = RemoveRecordMenu()

    print(f"Welcome to the {program_title}!\n{program_subtitle}.")
    time.sleep(2)

    while True:
        print(main_menu.display())
        print("Input a number and press ENTER to select an option.")
        while True:
            try:
                main_menu_input = int(input("Your input: "))
            except ValueError:
                print(f"Only INTEGERS from 1 to 4 are accepted!")
                continue
            else:
                break

        valid_main_menu_options = list(main_menu.get_options())

        # ADD NEW RECORD
        if main_menu_input == valid_main_menu_options[0]:
            time.sleep(1)
            print(add_record_menu.display())
            book_database.add_new_record()
            continue_to_main_menu()
            continue

        # DELETE A RECORD
        elif main_menu_input == valid_main_menu_options[1]:
            time.sleep(1)
            print(remove_record_menu.display())
            print("Input a number and press ENTER to select an option.")
            while True:
                try:
                    remove_record_menu_input = int(input("Your input: "))
                except ValueError:
                    print(f"Only INTEGER values between 1 and 4 accepted")
                    continue
                else:
                    break
            valid_remove_record_menu_options = list(remove_record_menu.get_options())
            # SEARCH BY TITLE
            if remove_record_menu_input == valid_remove_record_menu_options[0]:
                search_results = book_database.search_by_title()
            # SEARCH BY AUTHOR
            elif remove_record_menu_input == valid_remove_record_menu_options[1]:
                search_results = book_database.search_by_author()
            # SEARCH BY DATE
            elif remove_record_menu_input == valid_remove_record_menu_options[2]:
                search_results = book_database.search_by_date()
            # VIEW ALL RECORDS
            elif remove_record_menu_input == valid_remove_record_menu_options[3]:
                search_results = book_database.view_all_records()
            else:
                print("An unknown error occurred...")

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

        # VIEW ALL RECORDS
        elif main_menu_input == valid_main_menu_options[2]:
            print("Displaying records...")
            print("Book ID | Title | Author Name | Date Completed")
            print(book_database.view_all_records())
            continue_to_main_menu()
            continue

        # EXIT PROGRAM
        elif main_menu_input == valid_main_menu_options[3]:
            print("Exiting program...")
            exit_program()
        else:
            print("something went wrong")
        break
