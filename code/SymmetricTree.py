# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root is None:
            return True
        return helper(root.left, root.right)

def helper(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return a.val==b.val and helper(a.left, b.right) and helper(a.right, b.left)
        
