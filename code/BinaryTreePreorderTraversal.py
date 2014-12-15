# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
		re=[]
		if root==None:
			return re
		cur=root
		while cur!=None:
			if cur.left==None:
				re.append(cur.val)
				cur=cur.right
			else:
				pre=cur.left
				while pre.right!=None:
					pre=pre.right
				pre.right=cur.right
				cur.right=cur.left
				cur.left=None
		return re
        
