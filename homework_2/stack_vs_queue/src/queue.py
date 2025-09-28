from abstract_collection import AbstractCollection
from linked_list import LinkedList

class Queue(AbstractCollection):
    def __init__(self):
        self._list = LinkedList()
    
    def __len__(self):
        return len(self._list)
    
    def is_empty(self):
        return self._list.is_empty()
    
    def push(self, data):
        self._list.append_back(data)
    
    def pop(self):
        if self.is_empty():
            raise Exception("pop from empty queue")
        return self._list.pop_first()
    
    def peek(self):
        if self.is_empty():
            raise Exception("peek from empty queue")
        return self._list.peek_first()

