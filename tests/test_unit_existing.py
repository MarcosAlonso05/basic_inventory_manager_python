import pytest
from data import db_service
from auth import auth_service


def test_register_duplicate_user(monkeypatch):
    responses = iter(['admin', 'pass123'])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    result = auth_service.register_user()

    assert result is False


def test_add_category_success():
    cat_name = "Books"
    is_restricted = False

    success, msg = db_service.add_category(cat_name, is_restricted)

    assert success is True
    assert cat_name in db_service.inventory
    assert db_service.inventory[cat_name]['is_restricted'] is False


def test_delete_all_items_buggy_behavior():
    db_service.inventory['BugTest'] = {
        'items': ['Item1', 'Item2', 'Item3'],
        'is_restricted': False
    }

    db_service.delete_all_items_buggy('BugTest')

    remaining_items = db_service.inventory['BugTest']['items']

    assert len(remaining_items) > 0