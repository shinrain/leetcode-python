# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	# @param inorder, a list of integers
	# @param postorder, a list of integers
	# @return a tree node
	def buildTree(self, inorder, postorder):
		return helper(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1)

def helper(ind, il, ir, post, pl, pr):
	if il>ir:
		return None
	if il==ir:
		return TreeNode(ind[il])

	val = post[pr]
	i=ind.index(val)
	root=TreeNode(val)
	root.left = helper(ind, il, i-1, post, pl, i-1+pl-il)
	root.right = helper(ind, i+1, ir, post, pr+i-ir, pr-1)
	return root
        
