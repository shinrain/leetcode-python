# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root is None:
            return True
        else:
            if self.height(root) != -1:
                return True
            else:
                return False

    def height(self, root):
        # Return -1 if not balanced
        if root is None:
            return 0
        else:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            if left_height == -1 or right_height == -1:
                return -1
            else:
                if abs(left_height - right_height) <= 1:
                    return max(left_height, right_height) + 1
                else:
                    return -1
