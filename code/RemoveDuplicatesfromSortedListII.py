class Solution:
	# @param head, a ListNode
	# @return a ListNode
	def deleteDuplicates(self, head):
		if head is None or head.next is None:
			return head
		dummy = ListNode(0)
		tail = dummy
		while head is not None and head.next is not None:
			if head.val !=head.next.val:
				tail.next=head
				tail=head
				head=head.next
				tail.next=None
			else:
				head=remove(head)
		if head is not None:
			tail.next=head
		return dummy.next

def remove(head):
	if head is None and head.next is not None:
		return head

	val = head.val
	while head is not None:
		if head.val!=val:
			return head
		head=head.next
	return head
