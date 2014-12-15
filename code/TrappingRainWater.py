class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        n=len(A)
        if n<=2:
            return 0
        re=[0 for i in range(n)]
        re[0]=A[0]
        for i in range(1,n):
            re[i]=max(re[i-1], A[i])
        Max=A[n-1]
        res=0
        for i in range(n-2,0,-1):
            if A[i]>Max:
                Max=A[i]
            else:
                res+=(min(re[i],Max)-A[i])
        return res
