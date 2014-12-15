i# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
	def recoverTree(self, root):
		if root is None:
			return
		[first, second, pre, cur] = [None, None, None, root]
		while cur is not None:
			if cur.left is None:
				if pre is not None and pre.val>=cur.val:
					if first is None:
						[first, second]=[pre, cur]
					else:
						second = cur
				pre=cur
				cur=cur.right
			else:
				nex = cur.left
				while nex.right is not None and nex.right !=cur:
					nex=nex.right
				if nex.right is None:
					[nex.right, cur] = [cur, cur.left]
				else:
					nex.right=None
					if pre is not None and pre.val>=cur.val:
						if first is None:
							[first, second]=[pre, cur]
						else:
							second = cur

					pre=cur
					cur=cur.right
		if first is not None and second is not None:
			t=first.val
			first.val = second.val
			second.val=t
		return root
