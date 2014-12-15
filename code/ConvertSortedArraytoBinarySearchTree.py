# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
	# @param head, a list node
	# @return a tree node
	def sortedArrayToBST(self, num):
		n = len(num)
		if n==0:
			return None
		return helper(num, 0, n-1)

def helper(num, l, r):
	if l>r:
		return None
	if l==r:
		root=TreeNode(num[l])
		return root

	mid = l+(r-l)/2
	root = TreeNode(num[mid])
	root.left=helper(num, l, mid-1)
	root.right = helper(num, mid+1,r)
	return root


        
