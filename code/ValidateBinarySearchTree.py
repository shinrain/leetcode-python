# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @return a boolean
	def isValidBST(self, root):
		return helper(root, -(1<<32), (1<<32)-1)

def helper(root, Min, Max):
	
	if root is None:
		return True
	if root.val > Min and root.val<Max and helper(root.left, Min, root.val) and helper(root.right, root.val, Max):
		return True
	else:
		return False

