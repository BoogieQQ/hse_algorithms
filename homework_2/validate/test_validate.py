from main import validate

def test_example1():
    pushed = "1 2 3 4 5"
    popped = "1 3 5 4 2"
    assert validate(pushed, popped) == True

def test_example2():
    pushed = "1 2 3"
    popped = "3 1 2"
    assert validate(pushed, popped) == False

def test_same_order():
    pushed = "1 2 3 4 5"
    popped = "1 2 3 4 5"
    assert validate(pushed, popped) == True

def test_reverse_order():
    pushed = "1 2 3 4 5"
    popped = "5 4 3 2 1"
    assert validate(pushed, popped) == True

def test_invalid_sequence():
    pushed = "1 2 3 4 5"
    popped = "1 1 1 1 1"
    assert validate(pushed, popped) == False

def test_single_element():
    pushed = "1"
    popped = "1"
    assert validate(pushed, popped) == True

def test_single_element_invalid():
    pushed = "1"
    popped = "2"
    assert validate(pushed, popped) == False

def test_empty_sequences():
    pushed = ""
    popped = ""
    assert validate(pushed, popped) == True

def test_negative_numbers():
    pushed = "-1 -2 -3"
    popped = "-2 -1 -3"
    assert validate(pushed, popped) == True

def test_push_pop_alternating():
    pushed = "1 3 2 4"
    popped = "3 1 4 2"
    assert validate(pushed, popped) == True
