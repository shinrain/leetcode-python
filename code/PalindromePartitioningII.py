class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
    	n = len(s)
    	if n==0:
    		return 0
    	re=[n for i in range(n)]

    	for i in range(n):
    		MIN = n
    		for j in range(i, -1, -1):
    			if self.check(s[j:i+1]):
    				if j==0:
    					MIN=0
    					break;
    				else:
    					MIN=min(MIN, re[j-1])+1
    		re[i]=MIN
    	return re[n-1]

    def check(self, s):
    	[l,r]=[0,len(s)-1]
    	while l<r:
    		if s[l]!=s[r]:
    			return False
    		[l,r]=[l+1,r-1]
    	return True
