# lib/helpers.py
from models.comic import Comic
from models.character import Character

def exit_program():
    print("Goodbye!")
    exit()

# ============== COMIC FUNCTIONS ================

def create_comic():
    title = input("Enter the comic's title: ")
    main_character = input("Enter the main character: ")
    issue_number = input("Enter the issue number: ")
    universe = input("Enter the universe name: ")
    price = input("Enter the comic's price: ")
    try:
        comic = Comic.create(title, main_character, int(issue_number), universe, float(price))
        print(f'Success, {comic} added ')
    except Exception as exc:
        print("Error creating comic: ", exc)

def list_comics():
    comics = Comic.get_all()
    for comic in comics:
        print(comic)

def find_comic_by_id():
    id_ = input("Enter the comic's id: ")
    comic = Comic.find_by_id(id_)
    print(comic) if comic else print(f'Comic {id_} not found 🔍')

def delete_comic():
    id_ = int(input("Enter the comic's id: "))
    if comic := Comic.find_by_id(id_):
        comic.delete()
        print(f'Comic {id_} deleted 🗑️')
    else:
        print(f'Comic {id_} not found 🔍')
        

# ============ CHARACTER FUNCTIONS ==============

def create_character():
    name = input("Enter the character's name: ")
    secret_identity = input("Enter the character's secret identity: ")
    universe = input("Enter the character's universe: ")
    try:
        character = Character.create(name, secret_identity, universe)
        print(f'Success, {character} added')
    except Exception as exc:
        print("Error creating character: ", exc)

def delete_character():
    id_ = input("Enter the character's id: ")
    if character := Character.find_by_id(id_):
        character.delete()
        print(f'Character {id_} deleted')
    else:
        print(f'Character {id_} not found')
    
def find_character_by_id():
    id_ = input("Enter the character's id: ")
    if character := Character.find_by_id(id_):
       print(character) if character else print("Character id not found")

def list_characters():
    comics = Character.get_all()
    for comic in comics:
        print(comic)

def get_comics_by_secret_identity():
    secret_identity = input("Enter the character's secret identity: ")
    comics = Character.get_comics_by_secret_identity(secret_identity)
    if comics:
        for comic in comics:
            print(comic)
    else:
        print(f"No comics found for secret identity: {secret_identity}")