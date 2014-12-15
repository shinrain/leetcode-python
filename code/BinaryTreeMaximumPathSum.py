# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        self.max=root.val
        self.helper(root)
        return self.max
    
    def helper(self, root):
        if root ==None:
            return 0
        val = root.val
        left=self.helper(root.left)
        right=self.helper(root.right)
        if root.left!=None and root.right!=None:
            val = max(val, val+left)
            val = max(val, val+right)
        elif root.left==None:
            val = max(val, val+right)
        else:
            val = max(val, val+left)
        self.max=max(self.max, val)
        return max(root.val ,root.val+max(left, right))
        
