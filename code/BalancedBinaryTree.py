# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param root, a tree node
	# @return a boolean
	def isBalanced(self, root):
		return helper(root)!=-1

def helper(root):
	if root is None:
		return 0
	left = helper(root.left)
	right = helper(root.right)
	if left==-1 or right==-1 or abs(left-right)>1:
		return -1
	return max(left, right)+1
