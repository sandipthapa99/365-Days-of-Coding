# Data structure to store a binary tree node
class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
def postorder(root):
 
    # return if the current node is empty
    if root is None:
        return
 
    # Traverse the left subtree
    postorder(root.left)
 
    # Traverse the right subtree
    postorder(root.right)
 
    # Display the data part of the root or current node
    print(root.data, end=' ')
 
 
if __name__ == '__main__':
 
    """ Binary tree
               1
             /   \
            /     \
           2       3
          /      /   \
         /      /     \
        4      5       6
              / \
             /   \
            7     8
    """
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)
 
    postorder(root)

--------
Result:
--------------------------------------------------------
 4 2 7 8 5 6 3 1
--------------------------------------------------------