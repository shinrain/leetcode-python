class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        n=len(A)
        re=[]
        if n==0:
            return [-1,-1]
        [l,r]=[0,n-1]
        r1=-1
        while l<=r:
            mid=l+(r-l)/2
            if A[mid]==target:
                r1=mid
                r=mid-1
            elif A[mid]<target:
                l=mid+1
            else:
                r=mid-1
        if r1==-1:
            return [-1,-1]
        [l,r]=[0,n-1]
        r2=-1
        while l<=r:
            mid=l+(r-l)/2
            if A[mid]==target:
                r2=mid
                l=mid+1
            elif A[mid]<target:
                l=mid+1
            else:
                r=mid-1
        re=[r1,r2]
        return re
