class Solution:
    # @return an integer
    def totalNQueens(self, n):
        if n==0:
            return 0
        re=[0 for i in range(n)]
        return helper(re, 0)

def helper(re, k):
    if k==len(re):
        return 1
    val=0
    for i in range(len(re)):
        re[k]=i
        if check(re,k):
            val+=helper(re,k+1)   
    return val

def check(re,k):
    for i in range(k):
        if re[i]==re[k] or abs(re[i]-re[k])==k-i:
            return False
    return True
