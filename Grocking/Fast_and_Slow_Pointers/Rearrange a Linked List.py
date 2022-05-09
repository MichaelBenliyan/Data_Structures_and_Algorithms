from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(str(temp.value) + " ", end='')
      temp = temp.next
    print()

def rearrange(head): 
    slow, fast = head, head
    while fast is not None and fast.next is not None: 
        slow = slow.next
        fast = fast.next.next
    
    second_half_head = reverse(slow)
    copy_second_half_head = second_half_head
    
    first_half_head = head
    while second_half_head is not None: 
        skip_left = first_half_head.next
        next_up = second_half_head.next
        first_half_head.next = second_half_head
        second_half_head.next = skip_left
        second_half_head = next_up
        first_half_head = skip_left   
        
    if first_half_head is not None: 
        first_half_head.next = None
        
    # while head is not None: 
    #     print(head)
    #     head = head.next
    
    
def reverse(middle): 
    prev = None
    while middle is not None: 
        temp = middle.next
        middle.next = prev
        prev = middle
        middle = temp
    return prev


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)
  head.next.next.next.next.next = Node(12)
  rearrange(head)
  head.print_list()
  
main()