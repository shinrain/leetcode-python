# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        if head is None or head.next is None:
            return head
        dummy=ListNode(0)
        tail=dummy
        start=head
        
        while start is not None:
            cur = start
            count=1
            while cur.next is not None and count<k:
                count+=1
                cur=cur.next
            if count!=k:
                tail.next=start
                break
            t=cur.next
            cur.next=None
            tail.next=reverse(start)
            tail=start
            start=t
        return dummy.next

def reverse(head):
    if head is None and head.next is not None:
        return head
    newHead = None
    cur=head
    while cur is not None:
        t=cur.next
        cur.next=newHead
        newHead=cur
        cur=t
    return newHead
            
