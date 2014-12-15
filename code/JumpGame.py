class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        n=len(A)
        if n==0:
            return False
        if n==1:
            return True
        [start,end]=[0,0]
        while start<=end:
            Max = 0
            for i in range(start, end+1):
                Max=max(Max, i+A[i])
                if Max>=n-1:
                    return True
            start=end+1
            end=Max
        return False
