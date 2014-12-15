# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        n=len(lists)
        if n==0:
            return None
        if n==1:
            return lists[0]
        end = n-1
        while end>0:
            [l,r]=[0,end]
            while l<r:
                dm=ListNode(0)
                tl=dm
                [l1,l2]=[lists[l],lists[r]]
                while l1 is not None or l2 is not None:
                    if l1 is None:
                        tl.next=l2
                        break
                    if l2 is None:
                        tl.next=l1
                        break
                    if l1.val<=l2.val:
                        tl.next=l1
                        l1=l1.next
                        tl=tl.next
                        tl.next=None
                    else:
                        tl.next=l2
                        l2=l2.next
                        tl=tl.next
                        tl.next=None
                lists[l]=dm.next
                l+=1
                r-=1
            if l==r:
                end = l
            else:
                end=l-1
        return lists[0]
                
