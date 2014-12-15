class Solution:
	# @param n, an integer
	# @return an integer
	def climbStairs(self, n):
		if n==0:
			return 0
		if n==1:
			return 1
		[pre,cur]=[1,1]
		re=0
		for i in range(n-1):
			re=pre+cur
			pre=cur
			cur=re
		return re

