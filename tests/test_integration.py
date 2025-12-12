import pytest
from auth import auth_service
from data import db_service


def test_integration_login_and_restricted_access(monkeypatch):
    # Integracion: Login de usuario 'guest' -> intento de escritura restringida

    # 1. Simular Login
    responses = iter(['guest', 'guest123'])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    user_session = auth_service.login()

    assert user_session is not None
    assert user_session['role'] == 'observer'

    # 2. Usar el rol obtenido para intentar modificar datos
    category = 'Confidential'
    item = 'Hack'

    success, msg = db_service.add_item_restricted(category, item, user_session['role'])

    # Verificamos que la integracion de rol y DB funciona
    assert success is False
    assert "No tienes acceso" in msg


def test_integration_admin_workflow(monkeypatch):
    # Integracion: Login de admin -> modificacion exitosa

    # 1. Simular Login
    responses = iter(['admin', 'admin123'])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))

    user_session = auth_service.login()

    assert user_session['role'] == 'admin'

    # 2. Operacion de base de datos
    cat = 'Electronics'
    item = 'GPU'

    success, msg = db_service.add_item_restricted(cat, item, user_session['role'])

    assert success is True
    assert item in db_service.inventory[cat]['items']