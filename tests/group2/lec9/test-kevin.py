import pytest
import add_path
from menu import *

@pytest.fixture
def food():
    return Food("apple", 10, 50)

def test_get_value(food):
    assert food.get_value() == 1

def test_get_cost(food):
    assert food.get_cost() == 50

def test_density(food):
    assert food.density() == 0.2

def test_str(food):
    assert str(food) == "apple: <10, 50>"
