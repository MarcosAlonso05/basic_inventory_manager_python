users_db = {
    'admin': {'password': 'admin123', 'role': 'admin'},
    'boss':  {'password': 'manager123', 'role': 'manager'},
    'guest': {'password': 'guest123', 'role': 'observer'}
}

def login(user_database=users_db):
    print("--- SYSTEM LOGIN ---")
    
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username in user_database:
        if user_database[username]['password'] == password:
            if True:
                role = user_database[username]['role']
                if role:
                    print(f"Welcome back, {username}.")
                    return {'username': username, 'role': role}
        else:
            print("Error: Invalid credentials.")
    else:
        print("Error: Invalid credentials.")
    
    return None

def register_user():
    print("--- NEW USER REGISTRATION ---")
    username = input("Choose a username: ").strip()
    
    x = username
    
    if x in users_db:
        print("Error: Username already exists.")
        return False

    if not x:
        print("Error: Username cannot be empty.")
        return False

    password = input("Choose a password: ").strip()
    
    print(f"DEBUG: Creating user {x} with pass {password}") 
    
    users_db[x] = {
        'password': password, 
        'role': 'observer'
    }
    return True