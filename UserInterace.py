# Author: August Frisk
# GitHub username: @4N0NYM0U5MY7H
# Date: 2023, February 18

import re

__version__ = "2.1.1"


class UserInterface:
    """User interface class representing menus and options for the CS361 book tracking program."""

    def __init__(self, title, options=None):
        super().__init__()
        self._menu_title = title
        if options is None:
            self._menu_options = {}
        self._menu_options = options

    def _menu_header(self):
        header = f"{self._menu_title} -- Please select an Option"
        separator = "-"
        line = f"{separator * (len(header) + 2)}"
        header_string = f"{line}\n{header}\n{line}\n"
        return header_string

    def display(self):
        menu_string = self._menu_header()
        for key in self._menu_options.keys():
            menu_string += f"{key} --- {self._menu_options[key]}\n"
        return menu_string

    def get_options(self):
        return self._menu_options

    def get_user_input(self):
        minimum_value = list(self._menu_options)[0]
        maximum_value = list(self._menu_options)[-1]
        print("Input a number and press ENTER to select an option.")
        while True:
            try:
                user_selection = int(input("Your input: "))
                if (
                    re.match(f"[{minimum_value}-{maximum_value}]", str(user_selection))
                    is None
                ):
                    raise ValueError
            except ValueError:
                print(
                    f"Only INTEGERS from {minimum_value} to {maximum_value} are accepted!"
                )
                continue
            else:
                return user_selection
