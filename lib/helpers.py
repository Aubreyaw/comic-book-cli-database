# lib/helpers.py

from models.category import Category
from models.collectible import Collectible

def spacer(lines=1):
    print("\n" * lines)


def exit_program():
    print("Goodbye!")
    exit()


def choose_from_indexed_list(items, label_attr="name", prompt="Choose by number: "):
    for i, item in enumerate(items, 1):
        print(f"{i}. {getattr(item, label_attr)}")
    try:
        choice = int(input(prompt))
        return items[choice - 1]
    except (ValueError, IndexError):
        print("Invalid choice.")
        return None


def list_categories():
    categories = Category.get_all()
    if not categories:
        print("No categories found.")
        return []
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category.name}")
    return categories


def create_category():
    name = input("Enter the category name: ")
    try:
        category = Category.create(name)
        print(f'Success, {category.name} added ')
    except Exception as exc:
        print("Error creating category: ", exc)


def choose_category():
    categories = Category.get_all()
    if not categories:
        print("No categories available.")
        return None
    return choose_from_indexed_list(categories, label_attr="name", prompt="Select a category by number: ")


def list_collectibles(category):
    collectibles = Collectible.get_all()
    if not collectibles:
        print("No collectibles found")
        return []
    for i, collectible in enumerate(collectibles, 1):
        print(f"{i}. {collectible.name}")
    return collectibles


def choose_category_and_show_collectibles():
    categories = Category.get_all()
    category = choose_from_indexed_list(categories, label_attr="name", prompt="Choose a category by number: ")
    if not category:
        print("Category not found.")
        return None

    collectibles = category.get_collectibles()
    if not collectibles:
        print(f"No collectibles found in {category.name}.")
    else:
        print(f"\nCollectibles in {category.name}:")
        for i, collectible in enumerate(collectibles, 1):
            print(f"{i}. {collectible.name}")

    return category
        

def delete_category():
    categories = Category.get_all()
    category = choose_from_indexed_list(categories, label_attr="name", prompt="Select a category by number: ")
    if category:
        category.delete()
        print(f'Category "{category.name}" deleted ')
    else:
        print(f'Category not found ')


def create_collectible(category):
    name = input("Enter the collectible name: ")
    universe = input("Enter collectible's universe or property: ")
    est_value_str = input("Enter collectible's estimated value: $")
    
    try:
        est_value = float(est_value_str)
        collectible = Collectible.create(name, universe, est_value, category.id)
        print(f" Success! {collectible.name} was added to {category.name}.")

    except Exception as exc:
        print(" Error creating collectible: ", exc)


def delete_collectible(category):
    collectibles = category.get_collectibles()
    if not collectibles:
        print("No collectibles to delete in this category.")
        return
    
    collectible = choose_from_indexed_list(collectibles, label_attr="name", prompt="Choose a collectible to delete: ")

    if collectible:
        confirm = input(f"Are you sure you want to delete '{collectible.name}'? (y/n): ").lower()
        if confirm == "y":
            collectible.delete()
            print(f"{collectible.name} successfully deleted")
        else:
            print("Deletion canceled")
    else:
        print("Collectible not found")
    
  
def show_collectible_details(category):
        collectibles = category.get_collectibles()

        if not collectibles:
            print(f"No collectibles in {category.name}")
            return
        
        collectible = choose_from_indexed_list(collectibles, label_attr="name", prompt="Choose a collectible to view: ")
        print("")
        if collectible:
           details = collectible.display_details()
           for key, value in details.items():
               print(f"{key}: {value}")
        

def edit_collectible(category):
    collectibles = category.get_collectibles()
    collectible = choose_from_indexed_list(collectibles, label_attr="name", prompt="Choose a collectible to edit: ")

    if not collectible:
        return
    print(f"Editing '{collectible.name}' — press Enter to keep the current value.")

    new_name = input(f"[{collectible.name}] New name: ") or collectible.name
    new_universe = input(f"[{collectible.universe}] New universe or property: ") or collectible.universe
    new_value_input = input(f"[{collectible.est_value}] New estimated value: $") or collectible.est_value
    new_est_value = float(new_value_input) if new_value_input else collectible.est_value

    try:
        collectible.name = new_name
        collectible.universe = new_universe
        collectible.est_value = new_est_value
        collectible.update()
        print(f"{collectible.name} updated!")
    
    except Exception as exc:
        print("Error editing collectible: ", exc)