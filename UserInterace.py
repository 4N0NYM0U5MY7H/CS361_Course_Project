# Author: August Frisk
# GitHub username: @4N0NYM0U5MY7H
# Date: 2023, February 17
# Description: This file contains all the Menu interface classes
#              for the CS 361 Book Log program.

r"""User interface menus and options for the CS361 book tracking program.

Current menus are:
    Menu                 Base class for all other Menus.
    Main Menu            Primary interface for the program.
    Add Record Menu      Menu for adding new items to the database.
    Search Records Menu  Menu for searching the database.
    Delete Record Menu   Menu for removing items from the database.
"""

from abc import ABC, abstractmethod

__version__ = "1.1.1"


class _Menu(ABC):
    """Base Menu from which all other menus are derived."""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def _menu_header(self):
        pass

    @abstractmethod
    def display(self):
        pass


class MainMenu(_Menu):
    """Main Menu user interface and options."""

    def __init__(self):
        super().__init__()
        self._menu_title = "Main Menu"
        self._menu_options = {
            1: "Add a book to your records",
            2: "Search for a book",
            3: "View all books in your records",
            4: "Remove a book from your records",
            5: "Exit Program",
        }

    def _menu_header(self):
        """Returns a menu header string."""
        header = f"{self._menu_title} -- Please select an Option"
        separator = "-"
        line = f"{separator * (len(header) + 2)}"
        return f"{line}\n{header}\n{line}\n"

    def display(self):
        """Returns a menu interface string."""
        menu_string = self._menu_header()
        for key in self._menu_options.keys():
            menu_string += f"{key} --- {self._menu_options[key]}\n"
        return menu_string

    def get_options(self):
        """Returns all options for the current menu."""
        return self._menu_options


class AddRecordMenu(_Menu):
    """Add Record Menu interface and options."""

    def __init__(self):
        super().__init__()
        self._menu_title = "Add Record"
        self._menu_options = {
            "Book Title": "Title of the book",
            "Author Name": "First and last name of the author",
            "Date Completed": "Date the book was completed",
        }

    def _menu_header(self):
        """Returns a menu header string."""
        header = f"{self._menu_title} -- Please enter the following"
        separator = "-"
        line = f"{separator * (len(header) + 2)}"
        return f"{line}\n{header}\n{line}\n"

    def display(self):
        """Returns a menu interface string."""
        super().display()
        menu_string = self._menu_header()
        for key in self._menu_options.keys():
            menu_string += f"{key} --- {self._menu_options[key]}\n"
        return menu_string


class SearchRecordsMenu(_Menu):
    """Search Records Menu interface and options."""

    def __init__(self):
        super().__init__()
        self._menu_title = "Search Records"
        self._menu_options = {
            1: "Search by title of the book",
            2: "Search by author's name",
            3: "Search by date the book was completed",
            4: "View all entries",
        }

    def _menu_header(self):
        """Returns a menu header string."""
        header = f"{self._menu_title} -- Please select an Option"
        separator = "-"
        line = f"{separator * (len(header) + 2)}"
        return f"{line}\n{header}\n{line}\n"

    def display(self):
        """Returns a menu interface string."""
        menu_string = self._menu_header()
        for key in self._menu_options.keys():
            menu_string += f"{key} --- {self._menu_options[key]}\n"
        return menu_string

    def get_options(self):
        """Returns all options for the current menu."""
        return self._menu_options


class RemoveRecordMenu(_Menu):
    """Remove Record Menu interface and options."""

    def __init__(self):
        super().__init__()
        self._menu_title = "Remove Record"
        self._menu_options = {
            1: "Search by title of the book",
            2: "Search by author's name",
            3: "Search by date the book was completed",
            4: "View all entries",
        }

    def _menu_header(self):
        """Returns a menu header string."""
        header = f"{self._menu_title} -- Please select an Option"
        separator = "-"
        line = f"{separator * (len(header) + 2)}"
        return f"{line}\n{header}\n{line}\n"

    def display(self):
        """Returns a menu interface string."""
        super().display()
        menu_string = self._menu_header()
        for key in self._menu_options.keys():
            menu_string += f"{key} --- {self._menu_options[key]}\n"
        return menu_string

    def get_options(self):
        """Returns all options for the current menu."""
        return self._menu_options