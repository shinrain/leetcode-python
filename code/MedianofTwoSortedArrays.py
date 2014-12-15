class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        [m,n] = [len(A), len(B)]
        if (m+n)%2==0:
            return float(helper(A, 0, len(A)-1, B, 0, len(B)-1, (m+n)/2-1)+helper(A, 0, len(A)-1, B, 0, len(B)-1, (m+n)/2))/2
        else:
            return helper(A, 0, len(A)-1, B, 0, len(B)-1, (m+n)/2)
def helper(A, al, ar, B, bl, br, k):
    alen=ar-al+1
    blen=br-bl+1
    
    if alen==0:
        if blen<=k:
            return -1
        else:
            return B[bl+k]
    if blen==0:
        if alen<=k:
            return -1
        else:
            return A[al+k]
    amid=k*alen/(alen+blen)
    bmid=k-amid-1
    amid+=al
    bmid+=bl
    if A[amid]>B[bmid]:
        k-=(bmid-bl+1)
        bl=bmid+1
        ar=amid
    else:
        k-=(amid-al+1)
        al=amid+1
        br=bmid
    return helper(A, al, ar, B, bl, br, k)
