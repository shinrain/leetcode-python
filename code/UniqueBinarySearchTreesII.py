class Solution:
	# @return a list of tree node
	def generateTrees(self, n):
		if n==0:
			return [None]
		map={}
		return helper(1,n,n,map)

def helper(l, r, n, map):
	re=[]
	if l>r:
		return re
	if l==r:
		re.append(TreeNode(l))
		return re
	key = l*n+r
	if key in map:
		return map[key]

	for i in range(l,r+1):
		left = helper(l,i-1,n,map)
		right = helper(i+1,r,n,map)
		if len(left)==0:
			for ri in right:
				root=TreeNode(i)
				root.right=ri
				re.append(root)
		elif len(right)==0:
			for ll in left:
				root=TreeNode(i)
				root.left=ll
				re.append(root)
		else:
			for ll in left:
				for rr in right:
					root=TreeNode(i)
					root.left=ll
					root.right=rr
					re.append(root)
	map[key]=re
	return re
