class Solution:
	# @return an integer
	def numDistinct(self, S, T):
		[m,n]=[len(S), len(T)]
		if m==0:
			return 0
		if n==0:
			return 1
		re = [0 for i in range(n+1)]

		re[0]=1
		for i in range(m):
			for j in range(n, 0, -1):
				if S[i]==T[j-1]:
					re[j]+=re[j-1]
		return re[n]
