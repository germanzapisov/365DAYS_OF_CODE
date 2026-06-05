import pytest
from main import add, subtract, multiply

@pytest.fixture
def numbers():
    return {"a": 10, "b": 5}

def test_add(numbers):
    assert add(numbers["a"], numbers["b"]) == 15

def test_subtract(numbers):
    assert subtract(numbers["a"],numbers["b"]) == -1, "Не так"

def test_multiply(numbers):
    assert multiply(numbers["a"],numbers["b"]) == 50

