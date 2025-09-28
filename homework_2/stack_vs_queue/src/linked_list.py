class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.head is None
    
    def init_list(self, node):
        self.head = node
        self.tail = node
        self.size = 1
    
    def append_back(self, data):
        new_node = self.Node(data)
        if self.is_empty():
            self.init_list(new_node)
            return
        
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1
    
    def pop_back(self):
        if self.is_empty():
            raise Exception("pop_back from empty list")
        
        if self.head == self.tail:
            data = self.head.data
            self.head = None
            self.tail = None
            self.size = 0
            return data
                
        data = self.tail.data
        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1
        return data
    
    def pop_first(self):
        if self.is_empty():
            raise Exception("pop_first from empty list")
        
        data = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1
        
        if self.head is None:
            self.tail = None
        
        return data

    def peek_first(self):
        if self.is_empty():
            raise Exception("peek_first from empty list")
        return self.head.data
    
    def peek_last(self):
        if self.is_empty():
            raise Exception("peek_last from empty list")
        return self.tail.data
