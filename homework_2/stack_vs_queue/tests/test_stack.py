import sys
import os
import pytest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from stack import Stack

def test_stack_initialization():
    stack = Stack()
    assert len(stack) == 0
    assert stack.is_empty() is True

def test_push_single_element():
    stack = Stack()
    stack.push(123)
    assert len(stack) == 1
    assert stack.is_empty() is False

def test_push_multiple_elements():
    stack = Stack()
    elements = [1, 2, 3, 4, 5]
    
    for i, element in enumerate(elements):
        stack.push(element)
        assert len(stack) == i + 1
        assert stack.is_empty() is False

def test_pop_single_element():
    stack = Stack()
    stack.push(123)
    
    result = stack.pop()
    assert result == 123
    assert len(stack) == 0
    assert stack.is_empty() is True

def test_pop_multiple_elements_lifo():
    stack = Stack()
    elements = [1, 2, 3, 4, 5]
    
    for element in elements:
        stack.push(element)
    
    for expected in reversed(elements):
        assert stack.pop() == expected
    
    assert stack.is_empty() is True

def test_peek_single_element():
    stack = Stack()
    stack.push(123)
    
    assert stack.peek() == 123
    assert len(stack) == 1 
    assert stack.peek() == 123

def test_peek_multiple_elements():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1

def test_pop_empty_stack():
    stack = Stack()
    with pytest.raises(Exception) as exc_info:
        stack.pop()
    assert "empty stack" in str(exc_info.value).lower()

def test_peek_empty_stack():
    stack = Stack()
    with pytest.raises(Exception) as exc_info:
        stack.peek()
    assert "empty stack" in str(exc_info.value).lower()
