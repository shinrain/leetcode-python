class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n=len(A)
        if n<=1:
            return n
        [i,j]=[1,0]
        for j in range(1,n):
            if A[j]!=A[j-1]:
                A[i]=A[j]
                i+=1
        return i
        
