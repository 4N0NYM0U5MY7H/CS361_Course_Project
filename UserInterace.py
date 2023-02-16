# Author: August Frisk
# GitHub username: @4N0NYM0U5MY7H
# Date: 2023, February 15
# Description: This file contains all the Menu interface classes
#              for the CS 361 Book Log program.


__version__ = "1.1.0"


class Menu:
    """Represents a Menu object."""

    def __init__(self):
        pass

    def display(self):
        pass


class MainMenu(Menu):
    """Represents a Main Menu object."""

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
        """Return the Main Menu header."""
        header = f"{self._menu_title} -- Please select an Option"
        separator = "-"
        line = f"{separator * (len(header) + 2)}"
        return f"{line}\n{header}\n{line}\n"

    def display(self):
        """Returns the Main Menu."""
        super().display()
        menu_string = self._menu_header()
        for key in self._menu_options.keys():
            menu_string += f"{key} --- {self._menu_options[key]}\n"
        return menu_string

    def get_options(self):
        """Returns the Main Menu options."""
        return self._menu_options


class AddRecordMenu(Menu):
    """Represents the Add Record Menu."""

    def __init__(self):
        super().__init__()
        self._menu_title = "Add Record"
        self._menu_options = {
            "Book Title": "Title of the book",
            "Author Name": "First and last name of the author",
            "Date Completed": "Date the book was completed",
        }

    def _menu_header(self):
        """Returns the Add Record Menu header."""
        header = f"{self._menu_title} -- Please enter the following"
        separator = "-"
        line = f"{separator * (len(header) + 2)}"
        return f"{line}\n{header}\n{line}\n"

    def display(self):
        """Returns the Add Record Menu."""
        super().display()
        menu_string = self._menu_header()
        for key in self._menu_options.keys():
            menu_string += f"{key} --- {self._menu_options[key]}\n"
        return menu_string


class SearchRecordsMenu(Menu):
    """Represents the Search Records Menu."""

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
        """Returns the Search Records Menu header."""
        header = f"{self._menu_title} -- Please select an Option"
        separator = "-"
        line = f"{separator * (len(header) + 2)}"
        return f"{line}\n{header}\n{line}\n"

    def display(self):
        """Returns the Search Records Menu."""
        super().display()
        menu_string = self._menu_header()
        for key in self._menu_options.keys():
            menu_string += f"{key} --- {self._menu_options[key]}\n"
        return menu_string

    def get_options(self):
        """Returns the Search Records Menu options."""
        return self._menu_options


class RemoveRecordMenu(Menu):
    """Represents the Remove Record Menu."""

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
        """Returns the Remove Record Menu header."""
        header = f"{self._menu_title} -- Please select an Option"
        separator = "-"
        line = f"{separator * (len(header) + 2)}"
        return f"{line}\n{header}\n{line}\n"

    def display(self):
        """Returns the Remove Record Menu."""
        super().display()
        menu_string = self._menu_header()
        for key in self._menu_options.keys():
            menu_string += f"{key} --- {self._menu_options[key]}\n"
        return menu_string

    def get_options(self):
        """Returns the Remove Record Menu options."""
        return self._menu_options