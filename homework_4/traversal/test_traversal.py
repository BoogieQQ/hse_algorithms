from main import BST

def test_bst_main():
    bst = BST()
    
    values = [1, 3, 2, 4, 6, 5, 8, 7, 9, 0]
    for value in values:
        bst.insert(value)
    
    
    assert bst.in_order() == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    assert bst.pre_order() == [1, 0, 3, 2, 4, 6, 5, 8, 7, 9]
    
    assert bst.post_order() == [0, 2, 5, 7, 9, 8, 6, 4, 3, 1]
    
    assert bst.reverse_in_order() == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

    assert bst.reverse_pre_order() == [1, 3, 4, 6, 8, 9, 7, 5, 2, 0]
    
    assert bst.reverse_post_order() == [9, 7, 8, 5, 6, 4, 2, 3, 0, 1]

def test_bst_single():
    bst = BST()
    bst.insert(0)
    
    assert bst.in_order() == [0]
    assert bst.pre_order() == [0]
    assert bst.post_order() == [0]
    assert bst.reverse_in_order() == [0]
    assert bst.reverse_pre_order() == [0]
    assert bst.reverse_post_order() == [0]


def test_bst_empty():
    bst = BST()
    
    assert bst.in_order() == []
    assert bst.pre_order() == []
    assert bst.post_order() == []
    assert bst.reverse_in_order() == []
    assert bst.reverse_pre_order() == []
    assert bst.reverse_post_order() == []