# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

- Sort search search results.
- Update items in a database.
- Merge duplicate items in a database.
- Save a backup of the database.
- Load a backup of the database.
- Microservice integration to convert JSON data to an HTML document.
- View search results in a web browser.

## [2.0.0] - 2023-02-27 (expected)

### Added

- .gitattributes
- CHANGELOG.md
- Support for writing JSON files.
- Support for opening HTML files.
- BookLogDB can now output query results as a dictionary.
- 

### Changed

- Replaced the Menu classes with a single UserInterface class.
- Updated the project README.
- Full support for searching the database by author.
- Full support for searching the database by title.
- Full support for searching database by date.
- Renamed UserInterface.get_user_input to get_menu_selection.
- BookLogDB interface functions are no longer part of the database class (tentative).

## Removed

- Menu and Menu derived classes from the UserInterface module.

### Fixed

- BookLogDB connection method is now a private method.
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

[1.0.0]: https://github.com/4N0NYM0U5MY7H/CS361_Individual_Project/releases/tag/v1.0.0