class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        n=len(strs)
        if n==0:
            return ""
        i=0
        while i<len(strs[0]):
            val=strs[0][i]
            for s in strs:
                if i>=len(s) or s[i]!=val:
                    return s[0:i]
            i+=1
        return strs[0][0:i]
