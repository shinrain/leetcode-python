# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        d=ListNode(0)
        t=d
        while l1 is not None or l2 is not None:
            if l1 is None:
                t.next=l2
                break
            if l2 is None:
                t.next=l1
                break
            if l1.val<=l2.val:
                t.next=l1
                t=l1
                l1=l1.next
                t.next=None
            else:
                t.next=l2
                t=l2
                l2=l2.next
                t.next=None
        return d.next
