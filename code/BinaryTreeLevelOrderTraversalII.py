# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
	def levelOrderBottom(self, root):
		re=[]
		if root is None:
			return re
		q=[]
		q.append(root)
		start=0
		while len(q)>start:
			r=[]
			siz=len(q)
			for i in range(start, siz):
				cur = q[i]
				r.append(cur.val)
				if cur.left	is not None:
					q.append(cur.left)
				if cur.right is not None:
					q.append(cur.right)
			start=siz
			re.insert(0,r)
		return re
