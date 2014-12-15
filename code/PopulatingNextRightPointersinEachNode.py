# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
	# @param root, a tree node
	# @return nothing
	def connect(self, root):
		par=None
		cur = root
		helper(cur, par)
		while cur!=None:
			if cur.left!=None:
				par=cur
				cur=cur.left
				helper(cur, par)
			elif cur.right!=None:
				par=cur
				cur=cur.right
				helper(cur, par)
			else:
				cur=cur.next
def helper(root, par):
	if root==None:
		return
	if par==None:
		root.next=None
		return
	if root==par.left and par.right!=None:
		root.next=par.right
		helper(root.next, par)
		return
	
	while par.next!=None:
		par=par.next
		if par.left!=None:
			root.next=par.left
			helper(root.next, par)
			return
		elif par.right!=None:
			root.next=par.right
			helper(root.next,par)
			return
