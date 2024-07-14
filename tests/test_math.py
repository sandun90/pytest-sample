import pytest

products=[
    (2,3,6),(1,99,99),(0,99,0),(3,-4,-12)
]

@pytest.mark.parametrize('a,b,product',products)
def test_multiplication(a,b,product):
    assert a*b==product