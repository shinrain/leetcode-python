class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        n=len(A)
        if n==0:
            return 0
        [l,r]=[0,n-1]
        re=-1
        while l<=r:
            mid=l+(r-l)/2
            if A[mid]==target:
                return mid
            if A[mid]<target:
                re=mid+1
                l=mid+1
            else:
                re=mid
                r=mid-1
        return re
