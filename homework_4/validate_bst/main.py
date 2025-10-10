class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_valid_bst(root):
    def validate(node, min_val=float('-inf'), max_val=float('inf')):
        if not node:
            return True
        
        if node.value <= min_val or node.value >= max_val:
            return False 
        
        return (validate(node.left, min_val, node.value) and 
                validate(node.right, node.value, max_val))
    
    return validate(root)
