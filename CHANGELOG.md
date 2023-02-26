# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

- Sort search results.
- Update items in a database.
- Merge duplicate items in a database.
- Save a backup of the database.
- Load a backup of the database.

## [2.0.0] - 2023-02-26

### Added

- .gitattributes
- CHANGELOG.md
- BookDatabase.py
- utility.py
- Pipfile
- Support for writing JSON files.
- Support for opening HTML files in a web browser.
- BookDatabase can now output query results as a dictionary.
- Microservice integration to convert JSON data to an HTML document.
- View search results in a web browser.
- MicroserviceException class in case the microservice fails to respond.
- BookDatabase now creates a new database file if one does not exist.

### Changed

- Replaced the Menu classes with a single UserInterface class.
- Replaced the BookLogDB class with BookDatabase class.
- Updated the project README.
- Full support for searching database by author.
- Full support for searching database by title.
- Full support for searching database by date.
- Full support for searching database by id
- Renamed the UserInterface get_user_input method to get_user_selection.
- BookDatabase interface functions are no longer part of the database class.
- Repository architecture for organization.
- Moved various utility functions into their own module.

## Removed

- Menu and Menu derived classes from the UserInterface module.
- BookLogDB.py

### Fixed

- BookDatabase connection method is now a private method.
- Menu selection is now part of the UserInterface class.
- Minor corrections to the CHANGELOG.
- Refactored repeat code in the into functions.
- Issue with converting some queries to JSON ready dictionary.

## [1.0.0] - 2023-01-28

### Added

- User Interface design with the 8 Cognitive Style Heuristics.
- Feature to add items to a database.
- Feature to view all items in a database.
- Feature to remove items from a database.
- Basic support for searching a database.
- Encapsulated the user interface into Menu classes.
- Encapsulated database operations into it's own class.
- Project README.
- .gitignore

[2.0.0]: https://github.com/4N0NYM0U5MY7H/CS361_Individual_Project/releases/tag/v2.0.0
[1.0.0]: https://github.com/4N0NYM0U5MY7H/CS361_Individual_Project/releases/tag/v1.0.0