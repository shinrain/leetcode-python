# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
	def partition(self, head, x):
		if head is None or head.next is None:
			return head
		[d1,d2]=[ListNode(0), ListNode(0)]
		[t1,t2]=[d1,d2]
	
		while head is not None:
			if head.val<x:
				[t1.next, t1, head, t1.next]=[head, head, head.next, None]
			else:
				[t2.next, t2, head, t2.next]=[head, head, head.next, None]
		t1.next=d2.next
		return d1.next
        
