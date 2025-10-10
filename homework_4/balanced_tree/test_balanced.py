from main import is_balanced, Node

def test_empty_tree():
    assert is_balanced(None) == True

def test_single_node():
    root = Node(1)
    assert is_balanced(root) == True

def test_balanced_two_levels():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    assert is_balanced(root) == True

def test_unbalanced_left():
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)
    assert is_balanced(root) == False

def test_unbalanced_right():
    root = Node(1)
    root.right = Node(2)
    root.right.right = Node(3)
    assert is_balanced(root) == False

def test_balanced_diff_one():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    assert is_balanced(root) == True

def test_balanced_four_levels():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    assert is_balanced(root) == True
