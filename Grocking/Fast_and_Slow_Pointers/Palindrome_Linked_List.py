from numpy import array
from sqlalchemy import false, true


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def pll(node): 
    array = []
    count = 0
    i = node 
    while i != None: 
        count += 1
        array.append(i.value)
        i = i.next
    
    j = node
    k = len(array) - 1
    while j != None and k >= 0: 
        if j.value != array[k]: 
            return false
        else: 
            j = j.next
            k -= 1
    return True
        
def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  print(pll(head))
  
main()
    
    
    