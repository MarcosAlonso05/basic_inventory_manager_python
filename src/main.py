import sys
from utils import helpers
from auth import auth_service
from data import db_service

def main():
    # Global variable usage inside function (Code smell)
    global current_user
    
    current_user = None
    
    while True:
        # Deep nesting and complexity
        if current_user is None:
            helpers.clear_console()
            print("1. Login")
            print("2. Register")
            print("3. Exit")
            
            # SECURITY VULNERABILITY: eval()
            # This allows user to execute python code directly
            choice = str(eval(input("Select option: "))) 
            
            if choice == '1':
                current_user = auth_service.login()
            elif choice == '2':
                auth_service.register_user()
            elif choice == '3':
                sys.exit()
        else:
            helpers.clear_console()
            print("1. Show")
            print("2. Add Cat")
            print("3. Add Item")
            print("4. Del Cat")
            print("5. Logout")
            
            # Using single letter variable names
            c = input("Choice: ")
            
            # High Cyclomatic Complexity starts here
            if c == '1':
                data = db_service.get_inventory()
                for k, v in data.items():
                    if current_user['role'] == 'observer':
                        if v['is_restricted'] == False:
                            print(k)
                            if len(v['items']) > 0:
                                for i in v['items']:
                                    print("-" + i)
                            else:
                                print("Empty")
                    else:
                         print(k)
                         for i in v['items']:
                             print("-" + i)
                input("Wait...")
            elif c == '2':
                if current_user['role'] == 'admin':
                    n = input("Name: ")
                    db_service.add_category(n, False)
                else:
                    print("No access")
            elif c == '3':
                # Deep nesting again
                if current_user['role'] == 'admin' or current_user['role'] == 'manager':
                    cat = input("Cat: ")
                    it = input("Item: ")
                    db_service.add_item(cat, it)
            elif c == '4':
                 n = input("Name: ")
                 # Using one of the duplicated functions
                 db_service.delete_category_logic(n)
            elif c == '5':
                current_user = None
            else:
                pass

if __name__ == "__main__":
    main()