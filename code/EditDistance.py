class Solution:
	# @return an integer
	def minDistance(self, word1, word2):
		[m,n]=[len(word1), len(word2)]
		if m==0:
			return n
		if n==0:
			return m
		re=[i for i in range(n+1)]
		pre=0
		print re
		for i in range(m):
			for j in range(n+1):
				if j==0:
					pre=re[j]
					re[j]+=1
					# print pre, re[j]
				else:
					if word1[i]==word2[j-1]:
						t=re[j]
						re[j]=pre
						pre=t
					else:
						t=re[j]
						re[j]=min([re[j],re[j-1],pre])+1
						pre=t
		return re[n]
