# lib/cli.py

from helpers import (
    exit_program,
    create_comic,
    delete_comic,
    list_comics,
    find_comic_by_id,
    create_character,
    delete_character,
    list_characters,
    find_character_by_id,
    get_comics_by_secret_identity
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_comic()
        elif choice == "2":
            delete_comic()
        elif choice == "3":
            list_comics()
        elif choice == "4":
            find_comic_by_id()
        elif choice == "5":
            create_character()
        elif choice == "6":
            delete_character()
        elif choice == "7":
            list_characters()
        elif choice == "8":
            find_character_by_id()
        elif choice == "9":
            get_comics_by_secret_identity()
        else:
            print("😅 Oops! Please enter a number from the menu.")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create comic")
    print("2. Delete comic")
    print("3. List comics")
    print("4. Find comic by id")
    print("5. Create character")
    print("6. Delete character")
    print("7. List characters")
    print("8. Find character by id")
    print("9. List comics with characters sharing a secret identity")

if __name__ == "__main__":
    main()