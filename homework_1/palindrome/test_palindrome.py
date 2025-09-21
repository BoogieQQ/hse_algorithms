from main import is_palindrome


def test_one():
    assert is_palindrome(1)

def test_ten():
    assert not is_palindrome(10)

def test_odd():
    assert is_palindrome(101)

def test_even():
    assert is_palindrome(2002)

def test_not_odd():
    assert not is_palindrome(103)

def test_not_even():
    assert not is_palindrome(2012)

def test_small():
    assert is_palindrome(123321)

def test_big():
    assert is_palindrome(123456789987654321)