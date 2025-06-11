# Comic Book CLI Database

A command-line interface (CLI) application built with Python and SQLite that allows users to manage comic books and their characters, including features like creation, deletion, and querying based on shared universes or secret identities.

## Features
- Add, view, and delete comic books
- Add, view, and delete characters
- Link comics to characters by the main character's name
- Query all comics that feature a character with a certain secret identity
- Data validation and error handling for robust inputs

## Installation
Install my-project with git clone to clone the repository to your local environment:
```
https://github.com/Aubreyaw/python-p3-v2-final-project-template
```

### Prerequisites
- Python 3.8+
- SQLite3 (bundled with Python via `sqlite3` module)

### Run the CLI
```
python lib/cli.py
```
Follow the prompts to interact with the program!

### Example Usage
```
Please select an option:
1. Create comic
2. Delete comic
3. List comics
...
> 1
Enter the comic's title: The Amazing Spider-Man
Enter the main character: Spider-Man
Enter the issue number: 1
Enter the universe name: Marvel
Enter the comic's price: 3.99
Success, The Amazing Spider-Man, Spider-Man, 1, Marvel, price: 3.99 added
```

## Roadmap

- Provide a feature to update records (e.g., update a comic’s price).
- Data validation enhancements 
(e.g. validate unique comic titles, or restrict invalid characters in names)
- Enhanced search and filter options
(e.g. Enable users to search comics by title or character, or filter by universe or price range.)


## License

This project is open-source and available under the MIT License.
- Many-to-Many Relationships
Refactor the database schema to support many-to-many relationships (e.g., allow multiple characters per comic and vice versa), possibly through a join table like appearances

## Resources
- Class materials, lecture examples, and labs provided during Phase 3
- Official Python Documentation - https://www.python.org/
- SQLite3 Documentation - https://www.sqlite.org/docs.html

## Acknowledgements

- My instructors and peers for their valuable support.