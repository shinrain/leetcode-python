class Solution:
	# @return an integer
	def numTrees(self, n):
		if n==0:
			return 0
		if n==1:
			return 1
		re=[0 for i in range(n)]
		re[0]=1
		for i in range(1,n):
			re[i] = 2*re[i-1]
			for j in range(1, i):
				re[i] +=(re[j-1]*re[i-j-1])
		return re[n-1]
