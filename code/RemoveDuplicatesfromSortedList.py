# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	# @param head, a ListNode
	# @return a ListNode
	def deleteDuplicates(self, head):
		if head is None or head.next is None:
			return head
		dummy=ListNode(0)
		tail=dummy
		cur = head
		while cur is not None and cur.next is not None:
			t=cur.next
			tail.next=cur
			tail=cur
			tail.next=None
			if cur.val == t.val:
				t=remove(t)
			cur=t
		if cur is not None:
			tail.next=cur
		return dummy.next

def remove(head):
	if head is None or head.next is None:
		return None
	val = head.val
	while head is not None and val==head.val:
		head=head.next
	return head
        
