class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        n=len(A)
        if n==0:
            return 0
        [i,j]=[0,0]
        for j in range(n):
            if A[j]!=elem:
                A[i]=A[j]
                i+=1
        return i
