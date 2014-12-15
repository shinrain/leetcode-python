# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
	def postorderTraversal(self, root):
		re=[]
		if root==None:
			return re
		cur=TreeNode(0)
		cur.left=root
		while cur!=None:
			if cur.left==None:
				cur=cur.right
			else:
				pre=cur.left
				while pre.right!=None and pre.right!=cur:
					pre=pre.right
				if pre.right==None:
					pre.right=cur
					cur=cur.left
				else:
					pre.right=None
					t=cur.left
					n=len(re)
					while t!=None:
						re.insert(n,t.val)
						t=t.right
					cur=cur.right
		return re
        
