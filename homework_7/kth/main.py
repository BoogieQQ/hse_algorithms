import heapq

class MyHeap:
    def __init__(self):
        self.heap = []
    
    def upper(self, index):
        return (index - 1) // 2
    
    def left_child(self, index):
        return 2 * index + 1
    
    def right_child(self, index):
        return 2 * index + 2
    
    def swap(self, left, right):
        self.heap[left], self.heap[right] = self.heap[right], self.heap[left]
    
    def shift_up(self, index):
        upper = self.upper(index)
        while index > 0 and self.heap[index] < self.heap[upper]:
            self.swap(index, upper)
            index = upper
            upper = self.upper(index)
    
    def shift_down(self, index):
        n = len(self.heap)

        while True:
            right  = self.right_child(index)
            left   = self.left_child(index)
            curent = index

            if left < n and self.heap[left] < self.heap[curent]:
                curent = left
            
            if right < n and self.heap[right] < self.heap[curent]:
                curent = right
            
            if index == curent:
                return

            self.swap(index, curent)
            index = curent
        
    def push(self, value):
        self.heap.append(value)
        
        n = len(self.heap)
        self.shift_up(n - 1)
    
    def pop(self):
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.shift_down(0)
        
        return root
    
    def peek(self):
        return self.heap[0] if self.heap else None
    
    def size(self):
        return len(self.heap)

def my_kth(arr, k):
    heap = MyHeap()
    
    for e in arr:
        if heap.size() < k:
            heap.push(e)
        elif e > heap.peek():
            heap.pop()
            heap.push(e)
    
    return heap.peek()


def heapq_kth(arr, k):
    heap = []
    
    for e in arr:
        if len(heap) < k:
            heapq.heappush(heap, e)
        elif e > heap[0]:
            heapq.heappushpop(heap, e)
    
    return heap[0]
