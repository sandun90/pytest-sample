import pytest

def test_first_one():
    assert 1+1==2;

def test_first_two():
    assert 1+1==3;

def test_devided_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num=1/0
    assert 'division by zero' in str(e.value)