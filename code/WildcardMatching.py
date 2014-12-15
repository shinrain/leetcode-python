class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        n=len(p)
        if n==0:
            return len(s)==0
        [ss, star,i,j]=[0,-1,0,0]
        while i<len(s):
            if j<n and (s[i]==p[j] or p[j]=='?'):
                i+=1
                j+=1
            elif j<n and p[j]=='*':
                star=j
                ss=i
                i=ss
                j=star+1
            elif star!=-1:
                i=ss+1
                ss+=1
                j=star+1
            else:
                return False
        while j<n and p[j]=='*':
            j+=1
        return j==n
