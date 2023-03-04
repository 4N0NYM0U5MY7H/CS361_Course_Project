import os
import time
import json
import webbrowser
from Menu import Menu
from BookDatabase import (
    BookDatabase,
    enter_book_id,
    enter_book_title,
    enter_author_name,
    enter_date_completed,
    enter_filename,
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

__version__ = "1.5.4"
__author__ = "August Frisk <https://github.com/users/4N0NYM0U5MY7H>"


def search_records(database=BookDatabase, menu=Menu):
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


def backup_options(direrctory, database=BookDatabase, menu=Menu):
    valid_options = list(menu.get_options())
    selection = menu.get_menu_selection()

    if selection == valid_options[0]:
        return database.save_backup(f"{direrctory}/{enter_filename()}.db")
    elif selection == valid_options[1]:
        return database.load_backup(f"{direrctory}/{enter_filename()}.db")


if __name__ == "__main__":

    program_title = """
 /$$                           /$$       /$$             /$$    
| $$                          | $$      | $$            | $$    
| $$$$$$$   /$$$$$$   /$$$$$$ | $$   /$$| $$  /$$$$$$  /$$$$$$  
| $$__  $$ /$$__  $$ /$$__  $$| $$  /$$/| $$ /$$__  $$|_  $$_/  
| $$  \ $$| $$  \ $$| $$  \ $$| $$$$$$/ | $$| $$$$$$$$  | $$    
| $$  | $$| $$  | $$| $$  | $$| $$_  $$ | $$| $$_____/  | $$ /$$
| $$$$$$$/|  $$$$$$/|  $$$$$$/| $$ \  $$| $$|  $$$$$$$  |  $$$$/
|_______/  \______/  \______/ |__/  \__/|__/ \_______/   \___/
"""
    program_subtitle = "Tracking your reading since 2023"

    data_directory = "../data"
    os.makedirs(data_directory, exist_ok=True)

    microservice_request_file = "request.txt"
    microservice_request_data_file = "books.json"
    microservice_response_file = "response.html"
    database_file = "books.db"

    path_to_txt_file = f"{data_directory}/{microservice_request_file}"
    path_to_json_file = f"{data_directory}/{microservice_request_data_file}"
    path_to_html_file = f"{data_directory}/{microservice_response_file}"
    path_to_db_file = f"{data_directory}/{database_file}"

    book_database = BookDatabase(path_to_db_file)

    main_menu_options = {
        1: "ADD a book to your collection",
        2: "SEARCH your books",
        3: "VIEW ALL of your books",
        4: "REMOVE a book from your collection",
        5: "BACKUP options",
        6: "EXIT Program",
    }
    main_menu = Menu("Main Menu", main_menu_options)

    add_record_menu_options = {
        "Book Title": "Title of the book",
        "Author Name": "First and last name of the author",
        "Date Completed": "Date the book was completed",
    }
    add_record_menu = Menu("Add Record", add_record_menu_options)

    search_records_menu_options = {
        1: "Search by TITLE of the book",
        2: "Search by AUTHOR's name",
        3: "Search by DATE the book was completed",
        4: "VIEW ALL entries",
    }
    search_records_menu = Menu("Search Records", search_records_menu_options)
    remove_record_menu = Menu("Remove Record", search_records_menu_options)

    backup_menu_options = {
        1: "SAVE a backup of your collection",
        2: "LOAD a backup of your collection",
    }
    backup_menu = Menu("Backup Options", backup_menu_options)

    print(f"{program_title}\n{program_subtitle}.")
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

        # BACKUP OPTIONS
        elif main_menu_selection == valid_main_menu_options[4]:
            print(backup_menu.display())
            backup_options(data_directory, book_database, backup_menu)
            continue_to_main_menu()
            continue

        # EXIT PROGRAM
        elif main_menu_selection == valid_main_menu_options[-1]:
            print("Exiting program...")
            write_to_file("exit", path_to_txt_file)
            exit_program()
