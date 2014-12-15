# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
	def pathSum(self, root, sum):
		re=[]
		helper(root, sum, [],re)
		return re
	
def helper(root, sum, r, re):
	if root==None:
		return
	if root.left==None and root.right==None:
		if root.val==sum:
			r.append(root.val)
			re.append(r[:])
			r.pop()
		return
	r.append(root.val)
	helper(root.left, sum-root.val, r, re)
	helper(root.right, sum-root.val, r, re)
	r.pop()
