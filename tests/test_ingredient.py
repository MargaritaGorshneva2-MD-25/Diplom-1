import pytest
from praktikum.ingredient import Ingredient

@pytest.mark.parametrize("ingredient_type, name, price", [
    ("SAUCE", "Соус традиционный галактический", 50),
    ("FILLING", "Хрустящие минеральные кольца", 80)
])
def test_ingredient_type(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_type() == ingredient_type

@pytest.mark.parametrize("ingredient_type, name, price", [
    ("SAUCE", "Соус традиционный галактический", 50),
    ("FILLING", "Хрустящие минеральные кольца", 80)
])
def test_ingredient_name(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_name() == name

@pytest.mark.parametrize("ingredient_type, name, price", [
    ("SAUCE", "Соус традиционный галактический", 50),
    ("FILLING", "Хрустящие минеральные кольца", 80)
])
def test_ingredient_price(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_price() == price
