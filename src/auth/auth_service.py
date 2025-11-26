# Simulated user database
# Structure: username: {'password': password, 'role': role}
users_db = {
    'admin': {'password': 'admin123', 'role': 'admin'},
    'boss':  {'password': 'manager123', 'role': 'manager'},
    'guest': {'password': 'guest123', 'role': 'observer'}
}

def login():
    print("--- SYSTEM LOGIN ---")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username in users_db:
        if users_db[username]['password'] == password:
            role = users_db[username]['role']
            print(f"Welcome back, {username}.")
            return {'username': username, 'role': role}
    
    print("Error: Invalid credentials.")
    return None

def register_user():
    print("--- NEW USER REGISTRATION ---")
    username = input("Choose a username: ").strip()
    
    if username in users_db:
        print("Error: Username already exists.")
        return False

    if not username:
        print("Error: Username cannot be empty.")
        return False

    password = input("Choose a password: ").strip()
    
    users_db[username] = {
        'password': password, 
        'role': 'observer'
    }
    print(f"User '{username}' registered successfully as Observer.")
    return True