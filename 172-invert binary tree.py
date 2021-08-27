# A class to store a binary tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
 
 
# preorder traversal of the given binary tree
def preorder(root):
    if root is None:
        return
    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)
 
 
# swap left subtree with right subtree
def swap(root):
    if root is None:
        return
    temp = root.left
    root.left = root.right
    root.right = temp
 
 
# invert the binary tree using preorder traversal
def invertBinaryTree(root):
    # if the tree is empty
    if root is None:
        return
    # swap left subtree with right subtree
    swap(root)
    # invert left subtree
    invertBinaryTree(root.left)
    # invert right subtree
    invertBinaryTree(root.right)
 
if __name__ == '__main__':
 
    ''' Binary tree
              1
            /   \
           /     \
          2       3
         / \     / \
        4   5   6   7
    '''
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
 
    invertBinaryTree(root)
    preorder(root)

# --------
# Result:
# --------------------------------------------------------
# 1 3 7 6 2 5 4
# --------------------------------------------------------