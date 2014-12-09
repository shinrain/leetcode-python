#!/usr/bin/env python

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        if root == None:
        	return None

        re = []
        cur = root
        while cur!=None:
        	if cur.left==None:
        		re.append(cur.val)
        		cur = cur.right
        	else:
        		pre = cur.left
        		while pre.right!=None or pre.right!=cur:
        			pre = pre.right
        		if pre.right == None:
        			pre.right = cur
        			cur = cur.left
        		else:
        			pre.right = None
        			re.append(cur.val)
        			cur = cur.right
        return re


