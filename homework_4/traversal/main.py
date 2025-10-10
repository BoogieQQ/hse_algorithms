class BST:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
        
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = self.Node(value)
        else:
            self._insert(self.root, value)
    
    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = self.Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = self.Node(value)
            else:
                self._insert(node.right, value)
    
    def pre_order(self):
        # корень -> левое -> правое
        result = []
        self._pre_order(self.root, result)
        return result
    
    def _pre_order(self, node, result):
        if node is not None:
            result.append(node.value)
            self._pre_order(node.left, result)
            self._pre_order(node.right, result)
    
    def post_order(self):
        # левое -> правое -> корень
        result = []
        self._post_order(self.root, result)
        return result
    
    def _post_order(self, node, result):
        if node is not None:
            self._post_order(node.left, result)
            self._post_order(node.right, result)
            result.append(node.value)
    
    def in_order(self):
        # левое -> корень -> правое 
        result = []
        self._in_order(self.root, result)
        return result
    
    def _in_order(self, node, result):
        if node is not None:
            self._in_order(node.left, result)
            result.append(node.value)
            self._in_order(node.right, result)
    
    def reverse_pre_order(self):
        # корень -> правое -> левое
        result = []
        self._reverse_pre_order(self.root, result)
        return result
    
    def _reverse_pre_order(self, node, result):
        if node is not None:
            result.append(node.value)
            self._reverse_pre_order(node.right, result)
            self._reverse_pre_order(node.left, result)
    
    def reverse_post_order(self):
        # правое -> левое -> корень
        result = []
        self._reverse_post_order(self.root, result)
        return result
    
    def _reverse_post_order(self, node, result):
        if node is not None:
            self._reverse_post_order(node.right, result)
            self._reverse_post_order(node.left, result)
            result.append(node.value)
    
    def reverse_in_order(self):
        # правое -> корень -> левое
        result = []
        self._reverse_in_order(self.root, result)
        return result
    
    def _reverse_in_order(self, node, result):
        if node is not None:
            self._reverse_in_order(node.right, result)
            result.append(node.value)
            self._reverse_in_order(node.left, result)
