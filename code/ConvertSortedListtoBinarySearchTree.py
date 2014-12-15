class Solution:
    # @param head, a list node
    # @return a tree node
	def helper(self, l, r):
		if l>r:
			return None
		if l==r:
			root= TreeNode(self.list.val)
			self.list=self.list.next
		else:
			mid=l+(r-l)/2
			left=self.helper(l,mid-1)
			root=TreeNode(self.list.val)
			root.left=left
			self.list=self.list.next
			root.right=self.helper(mid+1,r)
		return root

	def sortedListToBST(self, head):
		if head is None:
			return None
		self.list=head
		count=0
		cur=head
		while cur.next is not None:
			count+=1
			cur=cur.next
		return self.helper(0, count)
