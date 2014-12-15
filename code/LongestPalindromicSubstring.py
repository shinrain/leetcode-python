class Solution:
    # @return a string
    def longestPalindrome(self, s):
        n=len(s)
        if n==0:
            return 0
        Max=0
        start=-1
        end=-1
        for i in range(n):
            [l,r]=[i,i]
            while l>=0 and r<n and s[l]==s[r]:
                r+=1
                l-=1
            if r-l-1>Max:
                Max=r-l-1
                start=l+1
                end=r-1

            
            [l,r]=[i,i+1]
            while l>=0 and r<n and s[l]==s[r]:
                r+=1
                l-=1
            if r-l-1>Max:
                Max=r-l-1
                start=l+1
                end=r-1
                
        return s[start:end+1]
