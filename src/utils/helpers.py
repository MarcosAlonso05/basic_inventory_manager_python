import os

def clear_console():
    # Clears the Terminal window
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)