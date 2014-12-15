class Solution:
	# @return a ListNode
	def removeNthFromEnd(self, head, n):
		if head is None:
			return head

		cur=head
		count=1
		while cur.next is not None and count<n:
			count+=1
			cur=cur.next
		if count<n:
			return head
		pre=None
		second=head
		while cur.next is not None:
			cur=cur.next
			pre=second
			second=second.next
		if pre is None:
			return second.next
		pre.next=second.next
		second.next=None
		return head

