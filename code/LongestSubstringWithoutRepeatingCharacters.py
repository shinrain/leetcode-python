class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        n=len(s)
        if n<=1:
            return n
        map={}
        [i,j]=[0,0]
        Max=0
        
        for j in range(n):
            if s[j] not in map:
                map[s[j]]=j
                Max=max(Max,j-i+1)
            else:
                if i<=map[s[j]]:
                    i=map[s[j]]+1
                map[s[j]]=j
                Max=max(Max,j-i+1)
        return Max
