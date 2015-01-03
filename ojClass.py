def construct(a):
	s=a[0]
	if len(s)==0:
		return None

	if s[0]=='#':
		a[0]=s[1::]
		return None
	else:
		root=TreeNode(int(s[0]))
		a[0]=s[1::]
		root.left=construct(a)
		root.right=construct(a)
		return root


# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
	def __str__(self):
		re=str(self.val)
		if self.left is None:
			re+="#"
		else:
			re+=str(self.left)
		if self.right is None:
			re+="#"
		else:
			re+=str(self.right)
		return re

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
		self.right = None
	def __str__(self):
		re=str(self.val)
		if self.next is not None:
			re+="->"+str(self.next)
		return re

class Point:
	def __init__(self, a=0, b=0):
		self.x = a
		self.y = b

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class UndirectedGraphNode:
	def __init__(self, x):
		self.label = x
		self.neighbors = []

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Interval:
	def __init__(self, s=0, e=0):
		self.start = s
		self.end = e
	def __str__(self):
		return "[%d,%d]"%(self.start, self.end)

