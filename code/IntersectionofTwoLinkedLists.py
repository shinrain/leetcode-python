# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA==None or headB==None:
            return None
        cur = headA
        while cur.next!=None:
            cur=cur.next
        mark=cur
        cur.next=headB
        
        nd1=headA
        nd2=headA
        count = 0
        while nd1.next!=None:
            count+=1
            nd1=nd1.next
            if count%2==0:
                nd2=nd2.next
                if nd1==nd2:
                    break;
        if nd1.next==None:
            if mark!=None:
                mark.next = None
            return None;
        nd1=headA
        while nd1!=nd2:
            nd1=nd1.next
            nd2=nd2.next
        if mark!=None:
            mark.next=None
        return nd1
        
        
        
