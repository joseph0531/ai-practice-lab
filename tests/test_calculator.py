from src.calculator import add, divide
import pytest


def test_add():
    print("---test---add---->>>>>")
    assert add(1, 2) == 3

def test_divide():
    print("---test---divide---->>>>>")
    assert divide(10, 2) == 5
