# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        carry=0
        dummy=ListNode(0)
        tail=dummy
        while l1 is not None or l2 is not None:
            val=carry
            if l1 is not None:
                val+=l1.val
                l1=l1.next
            if l2 is not None:
                val+=l2.val
                l2=l2.next
            tail.next=ListNode(val%10)
            tail=tail.next
            carry=val/10
        if carry!=0:
            tail.next=ListNode(carry)
        return dummy.next
            
