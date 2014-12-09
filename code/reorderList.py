class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head==None or head.next==None:
            return
        count = 0
        first = head
        second = head
        while first.next!=None:
            count+=1
            first = first.next
            if count%2==0:
                second = second.next
        first = second.next
        second.next = None
        self.merge(head, self.reverse(first))
    
    def merge(self, l1, l2):
        head = ListNode(0)
        tail = head;
        while l1!=None or l2!=None:
            if l1==None:
                tail.next = l2
                break
            if l2==None:
                tail.next = l1
                break
            t = l1
            l1=l1.next
            t.next = l2
            l2=l2.next
            tail.next = t
            tail = t.next
            tail.next = None
        return head.next
    
    def reverse(self, head):
        cur = head
        head = None
        while cur!=None:
            t = cur.next
            cur.next = head
            head = cur
            cur = t
        return head
