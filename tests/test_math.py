# This is a sample Python script.
import pytest


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def test_one_plus_one():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

data = [
    (2, 3, 6),
    (1, 99, 99),
    (0, 99, 0),
    (3, -4, -12),
    (-5, -5, 25),
    (2.5, 6.7, 16.75),
]


@pytest.mark.parametrize("a, b, result", data)
def test_multiply_two_number(a, b, result):
    assert a * b == result
