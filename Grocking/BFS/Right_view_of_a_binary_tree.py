
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

def tree_right_view(root): 
    solution = []
    queued_nodes = []
    queued_nodes.append(root)
    level_length = len(queued_nodes)
    while queued_nodes:
        for i in range(level_length): 
            node = queued_nodes[i]
            if node.left: 
                queued_nodes.append(node.left)
            if node.right: 
                queued_nodes.append(node.right)
        solution.append(node)
        for i in range(level_length): 
            queued_nodes.pop(0)
        level_length = len(queued_nodes)
    return solution

        
        



def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.left.left.left = TreeNode(3)
  result = tree_right_view(root)
  print("Tree right view: ")
  for node in result:
    print(str(node.val) + " ", end='')

main()