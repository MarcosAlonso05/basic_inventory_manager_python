# Simulated Inventory Structure
# Keys are category names. Values are dicts with 'items' (list) and 'is_restricted' (bool)
inventory = {
    'Electronics': {
        'items': ['Mouse', 'Keyboard'],
        'is_restricted': False
    },
    'Confidential': {
        'items': ['Prototype-X', 'Secret Docs'],
        'is_restricted': True  # Only Admin/Manager can see this
    }
}

def get_filtered_inventory(user_role):
    """
    Returns the inventory filtered by user permissions.
    Observers cannot see restricted categories.
    """
    if user_role == 'admin' or user_role == 'manager':
        return inventory
    
    # If observer, filter out restricted categories
    filtered_data = {}
    for category, details in inventory.items():
        if not details['is_restricted']:
            filtered_data[category] = details
    return filtered_data

def add_category(name, is_restricted):
    if name in inventory:
        return False, "Category already exists."
    
    inventory[name] = {
        'items': [],
        'is_restricted': is_restricted
    }
    return True, "Category added."

def delete_category(name):
    if name in inventory:
        del inventory[name]
        return True, "Category deleted."
    return False, "Category not found."

def add_item(category_name, item_name):
    if category_name in inventory:
        inventory[category_name]['items'].append(item_name)
        return True, "Item added."
    return False, "Category not found."