# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if root is None:
            return []
        q=[root]
        flg=False
        re=[]
        while len(q)!=0:
            siz=len(q)
            r=[]
            for i in range(siz):
                cur =q[0]
                q.remove(cur)
                if flg:
                    r.insert(0,cur.val)
                else:
                    r.append(cur.val)
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
            re.append(r)
            flg = not flg
        return re
        
