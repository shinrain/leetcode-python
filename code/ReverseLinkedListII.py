#!/usr/bin/env python
import sys, os

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
	def __str__(self):
		_str = str(self.val)
		if self.next!=None:
			_str+=str(self.next)
		return self.__name__
    def _str(self):
    	re = str(self.val)
    	cur = self.next
    	while cur!=None:
    		t = cur.next
    		re+=("->"+str(cur.val))
    		cur = t
    	return re

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
    	if head==None or head.next==None or m>=n:
    		return head

    	count = 0
    	l1=head
    	while l1.next!=None and count<n-m:
    		count+=1
    		l1=l1.next
    	
    	if count!=n-m:
    		return head
    	
    	pre = ListNode(0)
    	pre.next = head
    	head = pre
    	l2 = pre.next

    	count = 1
    	while l1.next!=None and count<m:
    		count+=1
    		l1=l1.next
    		pre	= l2
    		l2=l2.next
    	if count!=m:
    		return head

    	t = l1.next
    	l1.next = None
    	pre.next = self.reverse(l2)
    	l2.next = t
    	return head.next

    def reverse(self, head):
    	newhead =  None
    	cur = head
    	while cur!=None:
    		t = cur.next
    		cur.next = newhead	
    		newhead	 = cur
    		cur = t
    	return newhead



if __name__=='__main__':
	a = ListNode(1)
	b = ListNode(2)
	c = ListNode(3)
	a.next = b
	b.next = c
	print Solution().reverseBetween(a,1,2)._str()