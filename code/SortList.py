# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
	def sortList(self, head):
		if head==None or head.next==None:
			return head
		[n1,n2]=[head,head]
		count=0
		while n1.next!=None:
			count+=1
			n1=n1.next
			if count%2==0:
				n2=n2.next
		n1=n2.next
		n2.next=None

		return self.merge(self.sortList(head), self.sortList(n1))
	def merge(self, n1, n2):
		if n1==None:
			return n2
		if n2==None:
			return n1

		dummy=ListNode(0)
		tail=dummy
		while n1!=None or n2!=None:
			if n1==None:
				tail.next=n2
				break
			elif n2==None:
				tail.next=n1
				break
			else:
				if n1.val<=n2.val:
					tail.next=n1
					tail=n1
					n1=n1.next
				else:
					tail.next=n2
					tail=n2
					n2=n2.next
				tail.next=None
		return dummy.next
