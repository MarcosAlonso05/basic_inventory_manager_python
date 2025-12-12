import pytest
from data import db_service


def test_observer_cannot_add_to_restricted():
    category = 'Confidential'
    item = 'Spy Camera'
    user_role = 'observer'

    success, message = db_service.add_item_restricted(category, item, user_role)

    assert success is False
    assert "No tienes acceso" in message
    assert item not in db_service.inventory[category]['items']


def test_admin_can_add_to_restricted():
    category = 'Confidential'
    item = 'Admin Secret'
    user_role = 'admin'

    success, message = db_service.add_item_restricted(category, item, user_role)

    assert success is True
    assert item in db_service.inventory[category]['items']