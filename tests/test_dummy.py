import pytest

from dummy import calc, add, sub, mul


def test_add():
    assert add(1, 2) == 3


def test_sub():
    assert sub(3, 5) == -2


def test_mul():
    assert mul(3, 7) == 21


def test_calc():
    assert calc(1, '+', 2) == 3
    assert calc(3, '-', 5) == -2
    assert calc(3, 'x', 7) == 21
    assert calc(3, '.', 7) == 21
    assert calc(3, '*', 7) == 21

    with pytest.raises(Exception) as err_info:
        calc(3, '/', 7)
    assert 'dummy does not support this operation' in str(err_info.value)
