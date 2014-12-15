# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
	def insertionSortList(self, head):
		if head==None or head.next==None:
			return head
		dummy=ListNode(0)
		
		while head!=None:
			t=head.next
			head.next=None
			cur=dummy
			while True:
				if cur.next==None or cur.next.val>head.val:
					head.next=cur.next
					cur.next=head
					break
				else:
					cur=cur.next
			head=t
		return dummy.next
