# Simulated user database
# Format: username: {'password': password, 'role': role}
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
            print(f"Welcome, {username}. Role: {role.upper()}")
            return {'username': username, 'role': role}
    
    print("Error: Invalid credentials.")
    return None