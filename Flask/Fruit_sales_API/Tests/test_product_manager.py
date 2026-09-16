import sys
import os
from datetime import date

import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from managers.product_manager import ProductManager


@pytest.fixture
def manager():
    return ProductManager()


@pytest.fixture
def sample_product(manager):
    product = manager.create_product(
        name="Test Apple",
        price=1.50,
        entry_date=date.today(),
        quantity=100
    )
    yield product
    manager.delete_product(product.id)


def test_create_product(manager):
    product = manager.create_product(
        name="Test Banana",
        price=0.75,
        entry_date=date.today(),
        quantity=50
    )

    assert product.id is not None
    assert product.name == "Test Banana"
    assert product.quantity == 50

    manager.delete_product(product.id)


def test_update_product(manager, sample_product):
    updated = manager.update_product(sample_product.id, quantity=80)

    assert updated is not None
    assert updated.quantity == 80


def test_update_product_rejects_id_change(manager, sample_product):
    with pytest.raises(ValueError):
        manager.update_product(sample_product.id, id=9999)


def test_update_product_rejects_invalid_field(manager, sample_product):
    with pytest.raises(ValueError):
        manager.update_product(sample_product.id, quantityy=50)


def test_update_nonexistent_product_returns_none(manager):
    result = manager.update_product(999999, quantity=10)
    assert result is None


def test_get_all_products_includes_created(manager, sample_product):
    products = manager.get_all_products()
    ids = [p.id for p in products]

    assert sample_product.id in ids


def test_delete_product(manager):
    product = manager.create_product(
        name="Test Cherry",
        price=3.00,
        entry_date=date.today(),
        quantity=20
    )

    assert manager.delete_product(product.id) is True
    assert manager.delete_product(product.id) is False