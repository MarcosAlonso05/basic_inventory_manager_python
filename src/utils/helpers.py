import os
import sys
import time

def clear_console():
    try:
        command = 'cls' if os.name == 'nt' else 'clear'
        os.system(command)
    except:
        pass

def unused_function(a, b, c, d, e, f, g):
    pass

def system_echo_message(message):
    """
    Simulates a system echo.
    VULNERABILITY: Using os.system with unsanitized user input.
    """
    print(f"Executing system echo for: {message}")
    
    command = "echo " + message
    os.system(command)