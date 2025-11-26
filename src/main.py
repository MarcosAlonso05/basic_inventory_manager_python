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
            
            if not details['items']:
                print("  (Empty)")
            else:
                for item in details['items']:
                    print(f"  - {item}")
            print("-" * 20)
    
    input("\nPress Enter to continue...")

def handle_delete_item():
    print("--- Delete Specific Item ---")
    cat = input("Enter Category: ").strip()
    item = input("Enter Item Name to delete: ").strip()
    
    success, message = db_service.delete_item(cat, item)
    print(message)
    input("Press Enter...")

def authentication_flow():
    # Loop for Login or Register
    while True:
        helpers.clear_console()
        print("=== WELCOME TO INVENTORY SYSTEM ===")
        print("1. Login")
        print("2. Register (Guest Access)")
        print("3. Exit")
        
        choice = input("\nSelect option: ").strip()
        
        if choice == '1':
            user = auth_service.login()
            if user:
                return user
            input("Press Enter to try again...")
            
        elif choice == '2':
            auth_service.register_user()
            input("Press Enter to return to menu...")
            
        elif choice == '3':
            print("Goodbye.")
            sys.exit()

def main():
    # 1. Start Authentication
    current_user = authentication_flow()

    # 2. Main Application Loop
    while True:
        helpers.clear_console()
        role = current_user['role']
        print(f"=== MAIN MENU | User: {current_user['username']} ({role}) ===")
        
        print("1. Show Inventory")
        
        # Admin and Manager Controls
        if role in ['admin', 'manager']:
            print("2. Add Category")
            print("3. Add Item")
            print("4. Delete Category")
            print("5. Delete Specific Item")
        
        print("6. Logout / Exit")
        
        choice = input("\nSelect option: ").strip()
        
        if choice == '1':
            show_inventory(role)
            
        elif choice == '2':
            if role == 'observer':
                print("Access Denied.")
                input("Press Enter...")
            else:
                print("--- Add New Category ---")
                name = input("Category Name: ")
                if name:
                    restricted = input("Restricted? (y/n): ").lower() == 'y'
                    success, msg = db_service.add_category(name, restricted)
                    print(msg)
                input("Press Enter...")

        elif choice == '3':
            if role == 'observer':
                print("Access Denied.")
                input("Press Enter...")
            else:
                print("--- Add New Item ---")
                cat = input("Category: ")
                item = input("Item Name: ")
                if item:
                    success, msg = db_service.add_item(cat, item)
                    print(msg)
                input("Press Enter...")

        elif choice == '4':
            if role == 'observer':
                print("Access Denied.")
                input("Press Enter...")
            else:
                print("--- Delete Category ---")
                cat = input("Category to delete: ")
                success, msg = db_service.delete_category(cat)
                print(msg)
                input("Press Enter...")

        elif choice == '5':
            if role == 'observer':
                print("Access Denied.")
                input("Press Enter...")
            else:
                handle_delete_item()

        elif choice == '6':
            print("Logging out...")
            break

if __name__ == "__main__":
    main()