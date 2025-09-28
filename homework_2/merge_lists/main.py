class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    
    @classmethod
    def create(cls, data_list):
        linked_list = cls()        
        for data in data_list:
            linked_list.append_back(data)
        return linked_list

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
        
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def get_elems(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        
        return elements

def merge_two_lists_with_dummy(data1, data2):
    list1 = LinkedList.create(data1)
    list2 = LinkedList.create(data2)
    
    dummy = LinkedList.Node(0)
    
    current = dummy
    p1 = list1.head
    p2 = list2.head
    
    while p1 is not None and p2 is not None:
        if p1.data <= p2.data:
            current.next = p1
            p1 = p1.next
        else:
            current.next = p2
            p2 = p2.next
        current = current.next
    
    current.next = p1 if p1 is not None else p2

    merged = LinkedList()
    merged.head = dummy.next
    merged.size = 1 if merged.head is not None else 0 

    tail = merged.head
    while tail and tail.next:
        merged.size += 1
        tail = tail.next
    merged.tail = tail
        
    return merged


def merge_two_lists_without_dummy(data1, data2):
    list1 = LinkedList.create(data1)
    list2 = LinkedList.create(data2)

    if list1.is_empty():
        return list2
    if list2.is_empty():
        return list1
    
    if list1.head.data <= list2.head.data:
        head = list1.head
        p1 = list1.head.next
        p2 = list2.head
    else:
        head = list2.head
        p1 = list1.head
        p2 = list2.head.next
    
    current = head
    while p1 is not None and p2 is not None:
        if p1.data <= p2.data:
            current.next = p1
            p1 = p1.next
        else:
            current.next = p2
            p2 = p2.next
        current = current.next
    
    current.next = p1 if p1 is not None else p2
    
    merged = LinkedList()
    merged.head = head
    merged.size = 1 if merged.head is not None else 0 

    tail = merged.head
    while tail and tail.next:
        merged.size += 1
        tail = tail.next
    merged.tail = tail
        
    return merged
