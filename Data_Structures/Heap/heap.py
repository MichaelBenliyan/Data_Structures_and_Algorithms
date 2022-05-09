from turtle import right

class MinHeap: 
    def __init__(self, arr=[]) -> None:
        self.list = arr
        self.head = 0 
        if len(self.list) == 0: 
            self.tail = None
        else: 
            self.tail = len(self.list) - 1
            self.heapify()
    
    
    def heapify(self): 
        print("starting Heapify")
        current = self.tail 
        right = 2*(current+1)
        left = 2*(current+1)-1        
        while current >= 0: 
            if left > self.tail: 
                current -= 1
            elif right > self.tail: 
                if self.list[current] > self.list[left]: 
                    self.list[current], self.list[left] = self.list[left], self.list[current]
                current -= 1
            else: 
                if self.list[current] > self.list[left] or self.list[current] > self.list[right]:
                    lowest_child = min(self.list[left], self.list[right])
                    if lowest_child == self.list[left]: 
                        self.list[current], self.list[left] = self.list[left], self.list[current] 
                    else: 
                        self.list[current], self.list[right] = self.list[right], self.list[current]
                current -= 1
            right = 2*(current+1)
            left = 2*(current+1)-1  
    
    
    def peek(self): 
        return self.list[0]
    
    
    def pop_k(self, num_of_elements): 
        solution = []
        for _ in range(num_of_elements): 
            value = self.pop()
            solution.append(value)

            
    def bubble_up(self): 
        current = self.tail
        parent = (current-1)//2
        while current != 0 and self.list[current] < self.list[parent]: 
            self.list[current], self.list[parent] = self.list[parent], self.list[current]
            current = parent
            parent = (current-1)//2


    def trickle_down(self): 
        current = 0 
        right = 2*(current+1)
        left = 2*(current+1)-1
        while left < self.tail or right < self.tail: 
            if right < self.tail: 
                lowest_child = min(self.list[left], self.list[right]) #min(left,right, key=lambda x : self.list[x])
                if lowest_child < self.list[current]: 
                    if lowest_child == self.list[left]: 
                        self.list[current], self.list[left] = self.list[left], self.list[current]
                        current = left 
                    else: 
                        self.list[current], self.list[right] = self.list[right], self.list[current]
                        current = right  
                else: 
                    break
            else: 
                if self.list[left] < self.list[current]: 
                    self.list[current], self.list[left] = self.list[left], self.list[current]
                    current = left    
                else: 
                    break                               
            right = 2*(current+1)
            left = 2*(current+1)-1 


    def add(self, ele): 
        if self.tail is None: 
            self.tail = 0
            self.list.append(ele)  
        else: 
            self.list.append(ele)
            self.tail += 1
        self.bubble_up()  
    
    
    def pop(self): 
        self.list[self.head], self.list[self.tail] = self.list[self.tail], self.list[self.head]
        value = self.list.pop()
        self.trickle_down()
        return value


array = [4, 6, 9, 1, 5, 8, 1, 2, 8, 5]
# my_heap = MinHeap(array)
# print(my_heap.list)
# my_heap.add(0)
# print(my_heap.list)
# my_heap.pop()
# print(my_heap.list)
my_heap = MinHeap()
for i in array: 
    my_heap.add(i)
print(my_heap.list)
