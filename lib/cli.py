# lib/cli.py 

# list updated lists after creations, edits, and deletions

from helpers import (
    spacer,
    exit_program,
    create_category,
    list_categories,
    delete_category,
    list_collectibles,
    create_collectible,
    delete_collectible,
    show_collectible_details,
    edit_collectible
)

def main_menu():
    while True:
        main_menu_actions()
        choice = input(">  ")
        spacer(0)
        if choice == "x":
            exit_program()
        elif choice == "1":
            print("Categories:")
            list_categories()
            spacer(0)
            category_menu()
        else:
            print("😅 Oops! Please choose an option from the menu.")

def category_menu():
    category_menu_actions()
    choice = input(">  ")
    while choice != "b":
        spacer(0)
        if choice == "x":
            exit_program()
        elif choice == "1": 
           category = list_collectibles() 
           if category:
            collectible_menu(category)
            spacer(0)
        elif choice == "2":
            create_category()
            list_categories()
            spacer(0)
        elif choice == "3":
            delete_category()
            spacer(0)
        else:
            print("😅 Oops! Please choose an option from the menu.")
        category_menu_actions()
        choice = input(">  ")

def collectible_menu(category): 
    collectible_menu_actions()
    choice = input(">  ")
    while choice != "b":
        spacer(0)
        if choice == "x":
            exit_program()
        elif choice == "1":
            create_collectible(category)
            spacer(0)
        elif choice == "2":
            delete_collectible(category) 
            spacer(0) 
        elif choice == "3":
            show_collectible_details(category) 
            spacer(0)
        elif choice == "4":
            edit_collectible(category)
            spacer(0)
        else:
            print("😅 Oops! Please choose an option from the menu.")
        collectible_menu_actions()
        choice = input(">  ")

def main_menu_actions():
    print("\n************************************************")
    print("Welcome to the Collectibles Database!")
    print("Main menu: please select an option:")
    print(" Type 1 to list categories")
    print(" Type x to exit the program")
    print("************************************************")

def category_menu_actions():
    print("************************************************")
    print("Category Menu: please select an option:")
    print(" 1. View all collectibles in a category ")
    print(" 2. Create category ")
    print(" 3. Delete category ")
    print(" Type x to exit the program ")
    print(" Type b to go back to the main menu ")
    print("************************************************")

def collectible_menu_actions():
    print("\n************************************************")
    print("Collectible Menu: please select an option:")
    print(" 1. Add a collectible")
    print(" 2. Delete a collectible ")
    print(" 3. See collectible details")
    print(" 4. Edit collectible")
    print(" Type x to exit the program")
    print(" Type b to go back to the category menu")
    print("************************************************")

if __name__ == "__main__":
    main_menu()
    # 🚧