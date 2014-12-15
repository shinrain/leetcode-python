# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
	def copyRandomList(self, head):
		if head==None:
			return None
		cur = head
		while cur!=None:
			t=cur.next
			cur.next=RandomListNode(cur.label)
			cur.next.next=t;
			cur=t
		cur=head
		while cur!=None:
			if cur.random!=None:
				cur.next.random=cur.random.next
			else:
				cur.next.random=None
			cur=cur.next.next

		res=head.next
		cur=head
		while cur!=None:
			t=cur.next.next
			tt=cur.next
			if t==None:
				tt.next=None
			else:
				tt.next=t.next
			cur.next=t
			cur=t
		return res

        
