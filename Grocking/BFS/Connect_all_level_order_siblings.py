
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    def print_tree(self):
        print("Traversal using 'next' pointer: ", end='')
        current = self
        while current:
            print(str(current.val) + " ", end='')
            current = current.next

def connect_all_siblings(root): 
    queued_nodes = []
    queued_nodes.append(root)
    i = 0
    while i < len(queued_nodes): 
        node = queued_nodes[i]
        if node.left: 
            queued_nodes.append(node.left)
        if node.right: 
            queued_nodes.append(node.right)
        
        if i < len(queued_nodes)-1: 
            node.next = queued_nodes[i+1]
        else: 
            node.next = None
        i += 1


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_all_siblings(root)
  root.print_tree()

main()