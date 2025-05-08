import pytest
from praktikum.bun import Bun

@pytest.mark.parametrize("name, price", [
    ("white bun", 200),
    ("black bun", 150),
    ("red bun", 180)
])
def test_bun_name(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name

@pytest.mark.parametrize("name, price", [
    ("white bun", 200),
    ("black bun", 150),
    ("red bun", 180)
])
def test_bun_price(name, price):
    bun = Bun(name, price)
    assert bun.get_price() == price
