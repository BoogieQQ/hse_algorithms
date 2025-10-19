class AVL:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            self.height = 1
        
    def __init__(self):
        self.root = None
    
    def _get_height(self, node):
        if node is None:
            return 0
        return node.height
    
    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
    def _update_height(self, node):
        if node is not None:
            node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
    
    def _rotate_right(self, node_x):
        node_y = node_x.left
        tmp = node_y.right
        
        node_y.right = node_x
        node_x.left = tmp
        
        self._update_height(node_x)
        self._update_height(node_y)
        
        return node_y
    
    def _rotate_left(self, node_x):
        node_y = node_x.right
        tmp = node_y.left
        
        node_y.left = node_x
        node_x.right = tmp
        
        self._update_height(node_x)
        self._update_height(node_y)
        
        return node_y
    
    def _balance(self, node):
        self._update_height(node)
        
        balance = self._get_balance(node)
        
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._rotate_right(node)
        
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._rotate_left(node)
        
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node
    
    def insert(self, value):
        if self.root is None:
            self.root = self.Node(value)
        else:
            self.root = self._insert(self.root, value)
    
    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = self.Node(value)
            else:
                node.left = self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = self.Node(value)
            else:
                node.right = self._insert(node.right, value)
        
        return self._balance(node)
    
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def delete(self, value):
        self.root = self._delete(self.root, value)
    
    def _delete(self, node, value):
        if node is None:
            return node
        
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            tmp = self._min_value_node(node.right)
            node.value = tmp.value
            node.right = self._delete(node.right, tmp.value)
        
        return self._balance(node)
    
    def search(self, value):
        return self._search(self.root, value)
    
    def _search(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return node
        
        if value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)
        
    def is_balanced(self):
        return self._is_balanced(self.root)
    
    def _is_balanced(self, node):
        if node is None:
            return True
        
        balance = self._get_balance(node)
        return (abs(balance) <= 1 and 
                self._is_balanced(node.left) and 
                self._is_balanced(node.right))
