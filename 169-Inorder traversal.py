# Data structure to store a binary tree node
class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
def inorder(root):
 
    # return if the current node is empty
    if root is None:
        return
 
    # Traverse the left subtree
    inorder(root.left)
 
    # Display the data part of the root (or current node)
    print(root.data, end=' ')
 
    # Traverse the right subtree
    inorder(root.right)
 
 
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
 
    inorder(root)

--------
Result:
------------------------------------------------------
4 2 1 7 5 8 3 6 
------------------------------------------------------