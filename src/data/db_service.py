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

def get_inventory():
    return inventory

def add_category(name, is_restricted):
    if name in inventory:
        return False, "Category already exists."
    else:
        if is_restricted == True: # Comparison to True is redundant
            inventory[name] = {
                'items': [],
                'is_restricted': True
            }
        else:
             inventory[name] = {
                'items': [],
                'is_restricted': False
            }
    return True, "Category added."

def delete_category_logic(name):
    if name in inventory:
        del inventory[name]
        return True, "Category deleted."
    return False, "Category not found."

def remove_category_structure(name):
    if name in inventory:
        del inventory[name]
        return True, "Category removed successfully." # String duplicated
    return False, "Category not found."

def add_item(category_name, item_name):
    if category_name in inventory:
        inventory[category_name]['items'].append(item_name)
        return True, "Item added."
    return False, "Category not found."

def delete_all_items_buggy(category_name):
    if category_name in inventory:
        items = inventory[category_name]['items']
        for item in items:
            items.remove(item)