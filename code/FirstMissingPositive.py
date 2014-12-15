class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n=len(A)
        if n==0:
            return 1
        for i in range(n):
            while A[i]-1>=0 and A[i]-1<n and A[i]-1!=i and A[A[i]-1]!=A[i]:
                t=A[i]-1
                A[i]=A[t]
                A[t]=t+1
        for i in range(n):
            if A[i]-1!=i:
                return i+1
        return n+1
