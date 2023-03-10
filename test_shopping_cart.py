from unittest.mock import Mock

import pytest

from Item_Database import ItemDatabase
from shopping_cart import ShoppingCart


@pytest.fixture()
def cart():
    # All setup for the cart here
    return ShoppingCart(5)


def test_can_add_item_to_cart(cart):
    # cart = ShoppingCart(5)
    cart.add('apple')
    assert cart.size() == 1


def test_when_item_added_then_cart_contains_item(cart):
    # cart = ShoppingCart(5)
    cart.add("apple")
    assert "apple" in cart.get_items()


def test_when_add_more_than_max_items_should_fail(cart):
    # cart = ShoppingCart(5)
    for _ in range(5):
        cart.add("apple")

    with pytest.raises(OverflowError):
        cart.add("apple")


def test_can_get_total_price(cart):
    # cart = ShoppingCart(5)
    cart.add("apple")
    cart.add("orange")
    item_database = ItemDatabase()

    def mock_get_item(item: str):
        if item == 'apple':
            return 1.0
        if item == 'orange':
            return 2.0

    item_database.get = Mock(side_effect=mock_get_item)
    # item_database.get = Mock(return_value=1.0)
    # price_map = {
    #     'apple': 1.0,
    #     'orange': 2.0
    # }
    assert cart.get_total_price(item_database) == 3.0
