import sys
from utils import helpers
from auth import auth_service
from data import db_service

def show_inventory(user_role):
    print(f"--- Inventory (View Mode: {user_role.upper()}) ---")
    
    data = db_service.get_filtered_inventory(user_role)
    
    if not data:
        print("No categories available for your role.")
    else:
        for category, details in data.items():
            status = "[RESTRICTED]" if details['is_restricted'] else "[PUBLIC]"
            print(f"Category: {category} {status}")
            for item in details['items']:
                print(f"  - {item}")
            print("-" * 20)
    
    input("\nPress Enter to continue...")

def handle_add_category():
    print("--- Add New Category ---")
    name = input("Category name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    restricted_input = input("Is this restricted content? (y/n): ").lower().strip()
    is_restricted = True if restricted_input == 'y' else False

    success, message = db_service.add_category(name, is_restricted)
    print(message)
    input("\nPress Enter to continue...")

def main():
    helpers.clear_console()
    
    # 1. Login Loop
    current_user = None
    while not current_user:
        current_user = auth_service.login()
        if not current_user:
            retry = input("Try again? (y/n): ").lower()
            if retry != 'y':
                print("Exiting...")
                return
            helpers.clear_console()

    # 2. Main Menu Loop
    while True:
        helpers.clear_console()
        print(f"=== INVENTORY SYSTEM | User: {current_user['username']} ===")
        print("1. Show Inventory")
        
        # Only Admin and Manager can edit
        if current_user['role'] in ['admin', 'manager']:
            print("2. Add Category")
            print("3. Add Item")
            print("4. Delete Category")
        
        print("5. Exit")
        
        choice = input("\nSelect option: ").strip()
        
        if choice == '1':
            show_inventory(current_user['role'])
        
        elif choice == '2':
            if current_user['role'] == 'observer':
                print("Access Denied: Observers cannot add categories.")
                input("Press Enter...")
            else:
                handle_add_category()

        elif choice == '3':
            if current_user['role'] == 'observer':
                print("Access Denied: Observers cannot add items.")
                input("Press Enter...")
            else:
                # Simplified item adding logic for brevity
                cat = input("Category: ")
                item = input("Item name: ")
                success, msg = db_service.add_item(cat, item)
                print(msg)
                input("Press Enter...")

        elif choice == '4':
            if current_user['role'] == 'observer':
                print("Access Denied.")
            else:
                cat = input("Category to delete: ")
                success, msg = db_service.delete_category(cat)
                print(msg)
                input("Press Enter...")

        elif choice == '5':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()