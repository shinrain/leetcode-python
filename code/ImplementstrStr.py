class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        [m,n]=[len(haystack), len(needle)]
        if n==0:
            return 0
        if m==0:
            return -1
        [i,j]=[0,0]
        F=prefix(needle)
        while i<m:
            if j<n and haystack[i]==needle[j]:
                i+=1
                j+=1
                if j==n:
                    return i-n
            elif j==0:
                i+=1
            else:
                j=F[j]
        return -1
        
def prefix(p):
    n=len(p)
    if n==0:
        return []
    F=[0 for i in range(n+1)]
    F[0]=F[1]=0
    for i in range(2,n+1):
        j=F[i-1]
        while True:
            if p[i-1]==p[j]:
                F[i]=j+1
                break
            elif j==0:
                F[i]=0
                break
            else:
                j=F[j]
    return F
