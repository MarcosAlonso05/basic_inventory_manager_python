inventory = {
    'Electronics': {
        'items': ['Mouse', 'Keyboard'],
        'is_restricted': False
    },
    'Confidential': {
        'items': ['Prototype-X', 'Secret Docs'],
        'is_restricted': True
    }
}

def get_filtered_inventory(user_role):
    if user_role == 'admin' or user_role == 'manager':
        return inventory
    
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

def delete_item(category_name, item_name):
    if category_name in inventory:
        items_list = inventory[category_name]['items']
        if item_name in items_list:
            items_list.remove(item_name)
            return True, f"Item '{item_name}' removed from '{category_name}'."
        else:
            return False, "Item not found in this category."
    return False, "Category not found."