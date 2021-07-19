"""This module implements unit testing for module main.py"""

from unittest import mock
from datetime import datetime
import pytest
from software_testing.main import even_odd, sum_all, time_of_day, \
    Product, Shop


@pytest.mark.parametrize("test_number, expected", [
    (1, "odd"),
    (10, "even"),
    (-4, "even"),
    (1.0, "odd")
])
def test_even_odd(test_number, expected):
    assert even_odd(test_number) == expected


def test_even_odd_none_arg():
    test_number = None
    with pytest.raises(TypeError):
        even_odd(test_number)


@pytest.mark.parametrize("test_set_numbers, expected", [
    ([1, 2, 3], 6),
    ([1.0, 2.5], 3.5),
    ([-7, 2, 0], -5)
])
def test_func_sum(test_set_numbers, expected):
    assert sum_all(*test_set_numbers) == expected


def test_sum_none_arg():
    test_set_numbers = None
    with pytest.raises(TypeError):
        sum_all(test_set_numbers)


def test_sum_letters():
    test_letters = ["f", "l", "a", "s", "k"]
    with pytest.raises(TypeError):
        sum_all(*test_letters)


@pytest.mark.parametrize("test_arg_datetime, expected",
                         [
                             ([2021, 1, 1, 4, 0, 0], "night"),
                             ([2020, 1, 1, 6, 0, 0], "morning"),
                             ([2021, 1, 1, 15, 30, 0], "afternoon"),
                             ([2021, 1, 1, 22, 59, 0], "night"),
                         ]

                         )
@mock.patch("software_testing.main.datetime")
def test_datetime(mock_datetime, test_arg_datetime, expected):
    mock_datetime.now.return_value = datetime(*test_arg_datetime)
    assert time_of_day() == expected


@pytest.fixture
def common_product():
    return Product("common_product", 30, 10)


def test_subtract_quantity_without_args(common_product):
    common_product.subtract_quantity()
    assert common_product.quantity == 9


def test_subtract_quantity(common_product):
    common_product.subtract_quantity(4)
    assert common_product.quantity == 6


def test_add_quantity_without_args(common_product):
    common_product.add_quantity()
    assert common_product.quantity == 11


def test_add_quantity_with_quantity(common_product):
    common_product.add_quantity(7)
    assert common_product.quantity == 17


@pytest.mark.parametrize("test_price, expected",
                         [
                             (20, 20),
                             (19.99, 19.99),
                         ]
                         )
def test_change_price(common_product, test_price, expected):
    common_product.change_price(test_price)
    assert common_product.price == expected


@pytest.fixture
def product_without_quantity():
    return Product("product_without_quantity", 20.5)


def test_subtract_product_without_quantity(product_without_quantity):
    product_without_quantity.subtract_quantity()
    assert product_without_quantity.quantity == 0


def test_subtract_quantity_negative_case(product_without_quantity):
    with pytest.raises(TypeError):
        product_without_quantity.subtract_quantity("two")


def test_add_quantity_negative_case(product_without_quantity):
    with pytest.raises(TypeError):
        product_without_quantity.add_quantity("five")


@pytest.fixture
def empty_shop():
    return Shop()


@pytest.fixture
def shop_with_products(common_product, product_without_quantity):
    return Shop([common_product, product_without_quantity])


def test_empty_shop(empty_shop):
    assert empty_shop.products == []


def test_shop_add_product(empty_shop, common_product):
    empty_shop.add_product(common_product)
    assert empty_shop.products == [common_product]


def test_shop_add_new_product(empty_shop):
    empty_shop.add_product("new_product")
    assert empty_shop.products == ["new_product"]


def test_get_product_index(shop_with_products):
    assert shop_with_products._get_product_index("common_product") == 0


def test_get_product_wrong_index(shop_with_products):
    assert shop_with_products._get_product_index("not_exist_product") is None


def test_get_product_without_index(shop_with_products):
    with pytest.raises(TypeError):
        shop_with_products._get_product_index()


def test_sell_common_product(shop_with_products):
    assert shop_with_products.sell_product("common_product", 2) == 60


def test_sell_greater_then_available(shop_with_products):
    with pytest.raises(ValueError):
        shop_with_products.sell_product("common_product", 40)


@pytest.fixture
def shop_with_three_common_products():
    new_common_shop = Shop(Product("milk", 10, 20))
    new_common_shop.add_product(Product("water", 30, 40))
    return new_common_shop

def test_sell_product_money(shop_with_three_common_products):
    shop_with_three_common_products.sell_product("milk", 2)
    shop_with_three_common_products.sell_product("water", 10)
    assert shop_with_three_common_products.money == 320
