from main import AVL 


def test_avl_initialization():
    avl = AVL()
    assert avl.root is None
    assert avl.is_balanced() == True


def test_insert_into_empty_tree():
    avl = AVL()
    avl.insert(10)
    assert avl.root is not None
    assert avl.root.value == 10
    assert avl.root.height == 1
    assert avl.is_balanced() == True


def test_insert():
    avl = AVL()
    
    for value in range(5):
        avl.insert(value)
    
    for value in range(5):
        assert avl.search(value) is not None
        assert avl.search(value).value == value
    
    assert avl.is_balanced() == True

def test_search_nonexistent_values():
    avl = AVL()
    avl.insert(1)
    avl.insert(2)
    
    assert avl.search(3) is None
    assert avl.search(0) is None
    assert avl.is_balanced() == True


def test_delete_leaf_node():
    avl = AVL()
    avl.insert(1)
    avl.insert(2)
    avl.insert(3)
    
    avl.delete(3)
    assert avl.search(3) is None
    assert avl.search(1) is not None
    assert avl.search(2) is not None
    assert avl.is_balanced() == True


def test_delete_node_with_one_child():
    avl = AVL()
    avl.insert(5)
    avl.insert(4)
    avl.insert(3)
    avl.insert(2)
    
    avl.delete(4)
    assert avl.search(4) is None
    assert avl.search(5) is not None
    assert avl.search(3) is not None
    assert avl.search(2) is not None
    assert avl.is_balanced() == True


def test_delete_left_node_with_two_children():
    avl = AVL()
    values = [5, 3, 1, 2, 7, 6, 8]
    
    for value in values:
        avl.insert(value)
    
    avl.delete(3)
    assert avl.search(3) is None
    assert avl.search(1) is not None
    assert avl.search(2) is not None
    assert avl.is_balanced() == True

def test_delete_right_node_with_two_children():
    avl = AVL()
    values = [5, 3, 1, 2, 7, 6, 8]
    
    for value in values:
        avl.insert(value)
    
    avl.delete(7)
    assert avl.search(7) is None
    assert avl.search(6) is not None
    assert avl.search(8) is not None
    assert avl.is_balanced() == True


def test_delete_root_node():
    avl = AVL()
    avl.insert(1)
    avl.insert(2)
    avl.insert(3)
    
    avl.delete(2)
    assert avl.search(2) is None
    assert avl.search(1) is not None
    assert avl.search(3) is not None
    assert avl.is_balanced() == True


def test_delete_from_empty_tree():
    avl = AVL()
    avl.delete(1)
    assert avl.root is None
    assert avl.is_balanced() == True

def test_delete_nonexistent_value():
    avl = AVL()
    avl.insert(1)
    avl.insert(2)
    avl.insert(3)

    avl.delete(5)
    assert avl.search(1) is not None
    assert avl.search(2) is not None
    assert avl.search(3) is not None
    assert avl.is_balanced() == True


def test_balance_property():
    avl = AVL()
    
    values = [1, 2, 3, 4, 5, 6, 7]
    
    for value in values:
        avl.insert(value)
    
    assert avl._get_height(avl.root) <= 3
    
    for value in values:
        assert avl.search(value) is not None

    assert avl.is_balanced() == True


def test_left_rotations():
    avl = AVL()
    
    avl.insert(1)
    avl.insert(2)
    avl.insert(3) 
    
    assert avl.root.value == 2
    assert avl.root.left.value == 1
    assert avl.root.right.value == 3
    assert avl.is_balanced() == True

def test_right_rotations():
    avl = AVL()
    avl.insert(3)
    avl.insert(2)
    avl.insert(1)
    
    assert avl.root.value == 2
    assert avl.root.left.value == 1
    assert avl.root.right.value == 3
    assert avl.is_balanced() == True


def test_left_right_rotation():
    avl = AVL()
    avl.insert(3)
    avl.insert(1)
    avl.insert(2)
    
    assert avl.root.value == 2
    assert avl.root.left.value == 1
    assert avl.root.right.value == 3
    assert avl.is_balanced() == True


def test_right_left_rotation():
    avl = AVL()
    avl.insert(1)
    avl.insert(3)
    avl.insert(2) 
    
    assert avl.root.value == 2
    assert avl.root.left.value == 1
    assert avl.root.right.value == 3
    assert avl.is_balanced() == True


def test_height_calculation():
    avl = AVL()
    
    values = [1, 2, 3, 4, 5, 6, 7]
    heights = [1, 2, 2, 3, 3, 3, 3]
    
    for value, height in zip(values, heights):
        avl.insert(value)
        assert avl.root.height == height
        assert avl.is_balanced() == True
