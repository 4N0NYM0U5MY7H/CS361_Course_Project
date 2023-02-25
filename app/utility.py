import sys
import re
import time


__version__ = "1.1.0"

# --------------------------------------------------------------------
# Menu interface utility functions
def exit_program():
    return sys.exit()


def continue_to_main_menu():
    input("Press ENTER to continue...")
    print("Returning to Main Menu...")


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


# --------------------------------------------------------------------
# Microservice interface utility functions
class MicroserviceException(Exception):
    def __init__(self):
        self._message("The microservice failed to respond.")

    def __str__(self):
        return repr(self._message)


def wait_for_microservice_response(filename):
    print("Waiting for response from microservice...")
    max_attempts = 30
    attempt = 0
    while attempt < max_attempts:
        time.sleep(1)
        try:
            with open(filename, "r") as response:
                try:
                    response.readline()
                except OSError as error:
                    attempt += 1
                    continue
        except PermissionError as error:
            print(f"wait_for_microservice_response: {error}")
            return
        except FileNotFoundError:
            attempt += 1
            continue
        else:
            if attempt == max_attempts:
                raise MicroserviceException
            break


def write_to_file(data, filename):
    try:
        with open(filename, "w") as out_file:
            try:
                out_file.write(str(data))
            except OSError as error:
                print(f"write_to_file: {error}")
                continue_to_main_menu()
    except PermissionError as error:
        print(f"write_to_file: {error}")
        continue_to_main_menu()