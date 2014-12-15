# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        return self.helper(root, 0)
        
    def helper(self, root, pre):
        if root==None:
            return 0
        else:
            val = root.val+pre*10
            if root.left==None and root.right==None:
                return val
            else:
                return self.helper(root.left, val)+self.helper(root.right, val)

