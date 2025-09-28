import sys
import os
import pytest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from queue import Queue

def test_queue_initialization():
    queue = Queue()
    assert len(queue) == 0
    assert queue.is_empty() is True

def test_push_single_element():
    queue = Queue()
    queue.push(123)
    assert len(queue) == 1
    assert queue.is_empty() is False

def test_push_multiple_elements():
    queue = Queue()
    elements = [1, 2, 3, 4, 5]
    
    for i, element in enumerate(elements):
        queue.push(element)
        assert len(queue) == i + 1
        assert queue.is_empty() is False

def test_pop_single_element():
    queue = Queue()
    queue.push(123)
    
    result = queue.pop()
    assert result == 123
    assert len(queue) == 0
    assert queue.is_empty() is True

def test_pop_multiple_elements_fifo():
    queue = Queue()
    elements = [1, 2, 3, 4, 5]
    
    for element in elements:
        queue.push(element)
    
    for expected in elements:
        assert queue.pop() == expected
    
    assert queue.is_empty() is True

def test_peek_single_element():
    queue = Queue()
    queue.push(123)
    
    assert queue.peek() == 123
    assert len(queue) == 1 
    assert queue.peek() == 123

def test_peek_multiple_elements():
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    
    assert queue.pop() == 1
    assert queue.pop() == 2 
    assert queue.pop() == 3

def test_pop_empty_queue():
    queue = Queue()
    with pytest.raises(Exception) as exc_info:
        queue.pop()
    assert "empty queue" in str(exc_info.value).lower()

def test_peek_empty_queue():
    queue = Queue()
    with pytest.raises(Exception) as exc_info:
        queue.peek()
    assert "empty queue" in str(exc_info.value).lower()