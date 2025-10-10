class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_balanced(root):
    
    def check_balance(node):
        if not node:
            return True, 0
        
        left_balanced, left_height = check_balance(node.left)
        if not left_balanced:
            return False, None
        
        right_balanced, right_height = check_balance(node.right)
        if not right_balanced:
            return False, None
        
        if left_height is None or right_height is None or abs(left_height - right_height) > 1:
            return False, None
        
        current_height = max(left_height, right_height) + 1
        return True, current_height
    
    balanced, _ = check_balance(root)
    return balanced
