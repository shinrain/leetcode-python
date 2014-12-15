class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        map=["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        n=len(digits)
        if n==0:
            return [""]
        re=[]
        r=["." for i in range(n)]
        helper(digits, 0, r, re, map)
        return re

def helper(digits, k, r, re, map):
    if k==len(digits):
        re.append("".join(r))
    else:
        val=int(digits[k])-2
        for i in range(len(map[val])):
            r[k]=map[val][i]
            helper(digits, k+1,r,re,map)

        
