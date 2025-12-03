import pytest
import sys
import os


from data import db_service

@pytest.fixture(autouse=True)
def setup_inventory():
    # Reinicia el inventario antes de cada prueba
    db_service.inventory = {
        'Electronics': {
            'items': ['Mouse', 'Keyboard'],
            'is_restricted': False
        },
        'Confidential': {
            'items': ['Prototype-X'],
            'is_restricted': True
        }
    }