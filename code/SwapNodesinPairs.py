# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        d=ListNode(0)
        t=d
        cur=head
        while cur is not None and cur.next is not None:
            tt=cur.next.next
            t.next=cur.next
            cur.next.next=cur
            cur.next=None
            t=cur
            cur=tt
        if cur is not None:
            t.next=cur
        return d.next
