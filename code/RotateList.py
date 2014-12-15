class Solution:
	# @param head, a ListNode
	# @param k, an integer
	# @return a ListNode
	def rotateRight(self, head, k):
		if head is None or head.next is None or k==0:
			return head
		count=1
		cur=head
		while cur.next is not None and count<=k:
			count+=1
			cur=cur.next
		if count!=k+1:
			print count,k
			return self.rotateRight(head,k%count)
		first = head
		while cur.next is not None:
			cur=cur.next
			first=first.next

		cur.next=head
		head=first.next
		first.next=None
		return head
