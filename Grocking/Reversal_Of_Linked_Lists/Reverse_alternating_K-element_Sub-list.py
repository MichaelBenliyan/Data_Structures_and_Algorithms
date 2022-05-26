from __future__ import print_function
from unittest import skip


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


def reverse_alternating_k_sub_lists(head, k): 
    current, previous = head, None
    
    while current is not None:
        end_of_current_substring = current
        end_of_previous_substring = previous

        i = 0
        while current is not None and i < k: 
            next_node = current.next
            current.next = previous
            previous = current 
            current = next_node
            i += 1 

        if end_of_previous_substring is not None: 
            end_of_previous_substring.next = previous
        else: 
            head = previous
        end_of_current_substring.next = current

        skip = 0
        while current is not None and skip < k: 
            previous = current
            current = current.next
            skip += 1
    return head
    
def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_alternating_k_sub_lists(head, 2)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()
    
main()