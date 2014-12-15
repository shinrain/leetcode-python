# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
    	if head == None:
    		return head
    	elif head.next==head:
    		return head
        else:
        	[first, second]=[head, head]
        	count=0
        	while first!=None:
        		count+=1
        		first=first.next
        		if count%2==0:
        			second=second.next
        			if second==first:
        				break;
        	if first==None:
        	    return None
        	first=head
        	while first!=None:
        		[first, second]=[first.next, second.next]
        	return first
        
