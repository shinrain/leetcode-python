class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        n=len(A)
        if n==0:
            return 0
        re = -(1<<31)
        local=0
        for i in A:
            local+=i
            re=max(re,local)
            if local<0:
                local=0
        return re
