class Node: 
    def __init__(self, value) -> None:
        self.value = value
        self.prev = None
        self.next = None


class LinkedList: 
    def __init__(self) -> None:
        self.size = 0
        self.head = None
        self.tail = None
    
    def add(self, value): 
        node = Node(value)
        self.size += 1
        self.tail.next = node
        self.tail = node
        if self.size == 1: 
            self.head = node
        
    
    