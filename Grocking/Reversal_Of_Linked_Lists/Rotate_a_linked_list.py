
from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()

def rotate_linked_list(head, k): 
    current = head
    i = 1
    while current.next is not None: 
        current = current.next
        i += 1
    
    current.next = head

    start = i - k
    end = start -1
    start_location, end_location = head, head
    for i in range(start): 
        start_location = start_location.next
    
    head = start_location

    for i in range(end): 
        end_location = end_location.next

    end_location.next = None
    return head

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = rotate_linked_list(head, 3)
    print("Nodes of rotated LinkedList are: ", end='')
    result.print_list()


main()