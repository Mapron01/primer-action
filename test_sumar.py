import pytest
from Main import sumar

def test_sumar():
    assert sumar(3, 3) == 5

def test_restar():
    assert restar(4,2)== 2



def test_multiplicar():
    assert multiplicar(2,2) == 4

