# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
		if root==None:
			return root
		cur=root
		while cur!=None:
			if cur.left==None:
				cur=cur.right
			else:
				pre = cur.left
				while pre.right!=None:
					pre=pre.right
				pre.right = cur.right
				cur.right=cur.left
				cur.left=None
		return root
        
