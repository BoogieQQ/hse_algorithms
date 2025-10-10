import pytest
from main import Node, is_valid_bst

def test_empty_tree():
    assert is_valid_bst(None) == True

def test_single_node():
    root = Node(3)
    assert is_valid_bst(root) == True

def test_valid_bst_simple():
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    assert is_valid_bst(root) == True

def test_invalid_bst_simple():
    root = Node(3)
    root.left = Node(2) 
    root.right = Node(1)
    assert is_valid_bst(root) == False

def test_invalid_bst_simple_left():
    root = Node(3)
    root.left = Node(4) 
    root.right = Node(5)
    assert is_valid_bst(root) == False

def test_invalid_bst_simple_right():
    root = Node(3)
    root.left = Node(2) 
    root.right = Node(1)
    assert is_valid_bst(root) == False

def test_duplicate_values():
    root = Node(3)
    root.left = Node(2)
    root.right = Node(2)
    assert is_valid_bst(root) == False

def test_deep_tree_valid():
    root = Node(1)
    current = root
    for i in range(2, 25):
        current.right = Node(i)
        current = current.right
    assert is_valid_bst(root) == True

def test_deep_tree_invalid():
    root = Node(1)
    current = root
    for i in range(2, 25):
        current.left = Node(i)
        current = current.left
    assert is_valid_bst(root) == False
