class BSTNode:

  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

# function to check if it is an empty tree
def insert(value):
  
  if not root:
    root = BST(value)
  else:
    insertNode(root, value)

# recursive function to add the new node into the tree
def insertNode(current, value):

  # when the node value is greater than current node: go to right subtree
  if current.value < value:  
    if not current.right: # adding the node as a right node
      current.right = BSTNode(value) 
    else:
      insertNode(current.left, value) 
 
 # when the node value is smaller than current node: go to left subtree
  else:
    if not current.left: # adding the node as a left node
      current.left = BSTNode(value) 
    else:
      insertNode(current.right, value)

# visit left, root and right   3 7 9 2 4 8
def inOrderTraversal(root):
    
    if root: 
      inOrderTraversal(root.left)    # preOrderTraversal(3)   preOrderTraversal(2)   
      print(root.value)  # 7    3
      inOrderTraversal(root.right)   # preOrderTraversal(9)   preOrderTraversal()   

# visit root, left and right
def preOrderTraversal(root):
    
    if root:
      print(root.value)
      preOrderTraversal(root.left)
      preOrderTraversal(root.right)

# visit left, right and root
def postOrderTraversal(root):
    
    if root:
      postOrderTraversal(root.left)
      postOrderTraversal(root.right)
      print(root.value)

# checks either a value is in a BST or not
def contains(root, value):

  if not root: 
    return False

  if root.value == value:
    return True
  elif root.value < value:
    return contains(root.right, value)
  else:
    return contains(root.left, value)

# return the parent node if it exists    
def findParent(root, value):

  if not root:
    return None

  if value < root.value: 
    if not root.left:
      return None
    elif root.left.value == value:
      return root.value
    else:
      return findParent(root.left, value)  #3,  1

  else: # value > root.value 
    if not root.right:
      return None
    elif root.right.value == value:
      return root.value
    else: 
      return findParent(root.right, value)

# def breadthFirst(root):
#   queue = []
#   while root:
#     print(root)

#     if root.left:
#       queue.append(root.left.value)

#     if root.right:
#       queue.append(root.right.value)

#     if queue:
#       root = queue.pop(0)
#     else:
#       root = None


print(" A Binary Search Tree")
print("     6")
print("   /   \ ")
print("  3     8")
print(" / \     \\")
print(" 1  4    10")

root = BSTNode(6)
root.left = BSTNode(3)
root.right = BSTNode(8)
root.left.left = BSTNode(1)
root.left.right = BSTNode(4)
root.right.right = BSTNode(10)

print("InorderTraversal of a binary SEARCH tree: ")
inOrderTraversal(root)
print("PreorderTraversal of a binary tree: ")
preOrderTraversal(root)
print("PostorderTraversal of a binary tree: ")
postOrderTraversal(root)

#print(contains(root, 11))
print(findParent(root, 6))
print(breadthFirst(root))


print(" A Binary Search Tree")
print("     7")
print("   /   \ ")
print("  3     15")
print("        / \\")
print("       9    20")

root = BSTNode(7)
root.left = BSTNode(3)
root.right = BSTNode(15)
root.right.left = BSTNode(9)
root.right.right = BSTNode(20)

print("InorderTraversal of a binary SEARCH tree: ")
inOrderTraversal(root)
print("PreorderTraversal of a binary tree: ")
preOrderTraversal(root)
print("PostorderTraversal of a binary tree: ")
postOrderTraversal(root)








    
