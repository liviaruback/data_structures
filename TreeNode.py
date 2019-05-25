# Program for tree traversals

# A node in a binary tree
class TreeNode:

	def __init__(self, data = None):
		self.left = None
		self.right = None
		self.data = data

	def __repr__(self):
		return self.data

# A function to do inorder tree traversal
def printInOrder(node):
	if node:
		# First visit the left node 
		printInOrder(node.left)

		# Print the data of node
		print(node.data)

		# Then visit the right node
		printInOrder(node.right)

# A function to do preOrder tree traversal - visits the current node before its childs
def printPreOrder(node):
	if node:
		# First visit the current node 
		print(node.data)
		
		# Then visit the left node
		printPreOrder(node.left)

		# Then visit the right node
		printPreOrder(node.right)

# A function to do postOrder tree traversal - visits the current node after its childs
def printPostOrder(node):
	if node:
		# First visit the left node
		printPreOrder(node.left)

		# Then visit the right node
		printPreOrder(node.right)

		# Then visit the current node 
		print(node.data)

# A function to create a balanced search tree from a sorted array
def sortedArrayToBST(arr):

	if not arr: return None

	# find the middle number
	middle = len(arr) // 2

	# create the nodes
	node = TreeNode(arr[middle])

	# left subtree has all values < arr[mid]
	node.left = sortedArrayToBST(arr[:middle])

	# right subtree has all values > arr[mid]
	node.right = sortedArrayToBST(arr[middle+1:])

	return node

# A function to height a node
def height(node):

	if node: 
		return 1 + max(height(node.left), height(node.right))
	else:
		return 0
		
print(" A Binary Tree")
print("    0")
print("  /  \ ")
print("  1   2")
print("     / \\")
print("     3  4")

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)

print("InorderTraversal of a binary tree: ")
printInOrder(root)
print("PreorderTraversal of a binary tree: ")
printPreOrder(root)
print("PostorderTraversal of a binary tree: ")
printPostOrder(root)

print(" A Binary Search Tree")
print("     5")
print("   /   \ ")
print("  4     8")
print(" / \     \\")
print(" 1  3    10")

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.right = TreeNode(10)

print("InorderTraversal of a binary SEARCH tree: ")
printInOrder(root)
print("PreorderTraversal of a binary tree: ")
printPreOrder(root)
print("PostorderTraversal of a binary tree: ")
printPostOrder(root)

arr = [1,2,3,4,5,6,7]
bst = sortedArrayToBST(arr)
print("InorderTraversal of a bst from a sorted array ")
printInOrder(bst)

print("The height of the tree...")
print(height(bst))
