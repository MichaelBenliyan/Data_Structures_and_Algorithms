class Que: 
    def __init__(self, max_size) -> None:
        self.max_size = max_size
        self.size = 0
        self.list = [x for x in range(15)]
        self.head_idx = 0
        self.tail_idx = -1
        self.head = self.list[self.head_idx]
        self.tail = self.list[self.tail_idx]
    
    def isFull(self): 
        return self.size == self.max_size
        
    def isEmpty(self): 
        return self.size == 0
        
    def size(self): 
        return self.size
    
    def insert(self, new_ele): 
        if not self.isFull(): 
            if self.isEmpty(): 
                self.head_idx = 0
                self.tail_idx = -1
                self.list.insert((self.tail_idx+1) % self.max_size, new_ele)
                self.size += 1
                self.tail_idx += 1
                self.tail = self.list[self.tail_idx % self.max_size]
                self.head = self.list[self.head_idx % self.max_size]
            else:   
                self.list.insert((self.tail_idx+1) % self.max_size, new_ele)
                self.tail_idx += 1
                self.tail = self.list[self.tail_idx % self.max_size]
                self.size += 1
            return True
        else: 
            return False
        
    def delete(self): 
        if not self.isEmpty(): 
            if self.size == 1: 
                self.size = 0
                x = self.head
                self.head_idx = -1
                self.tail_idx = -1
                self.head = self.list[self.head_idx % self.max_size]
                self.tail = self.list[self.tail_idx % self.max_size]
                return x
            else: 
                x = self.head
                self.size -= 1
                self.head_idx += 1
                self.head = self.list[self.head_idx % self.max_size]
                return x
        else: 
            return False
        
    
my_que = Que(2)
print(my_que.insert("jack"))
print(my_que.insert("jill"))
print(my_que.insert("joe"))
print(my_que.delete())
print(my_que.delete())
print(my_que.delete())
print(my_que.delete())
print(my_que.insert("jack"))
print(my_que.insert("jill"))
print(my_que.insert("joe"))
