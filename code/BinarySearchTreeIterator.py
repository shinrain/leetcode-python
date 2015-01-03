i# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.cur=root

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if self.cur is None:
            return False
        if self.cur.left is None:
            return True
        while self.cur is not None:
            if self.cur.left is None:
                break
            pre=self.cur.left
            while pre.right is not None and pre.right !=self.cur:
                pre=pre.right
            if pre.right is None:
                pre.right=self.cur
                self.cur=self.cur.left
            else:
                self.pre=pre
                break
        return self.cur is not None
    # @return an integer, the next smallest number
    def next(self):
        if self.cur.left is None:
            re=self.cur.val
            self.cur=self.cur.right
        else:
            self.pre.right=None
            re=self.cur.val
            self.cur=self.cur.right
        return re
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
