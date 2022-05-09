class Stack(): 
    def __init__(self, max_size) -> None:
        self.max_size = max_size
        self.size = 0
        self.list = []
    
    def isFull(self): 
        return self.size == self.max_size

    def isEmpty(self): 
        return self.size == 0 
    
    def size(self): 
        return self.size
    
    def push(self, new_ele): 
        if not self.isFull():
            self.list.append(new_ele)
            self.size += 1
            return True
        else: 
            return False
        
    def pop(self): 
        if not self.isEmpty():  
            self.size -= 1
            return self.list.pop()
        else: 
            return False
        
    def peek(self): 
        return self.list[-1]
    
            

my_stack = Stack(5)
my_stack.push(5)
my_stack.push(6)
print(my_stack.size)
print(my_stack.pop())
print(my_stack.size)
print(my_stack.peek())
print(my_stack.isFull())
print(my_stack.isEmpty())