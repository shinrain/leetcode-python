class Solution:
	# @return a boolean
	def isInterleave(self, s1, s2, s3):
		m=len(s1)
		n=len(s2)
		if m+n!=len(s3):
			return False
		if m==0:
			return s2==s3
		if n==0:
			return s1==s3
		re=[False for i in range(n+1)]
		re[0]=True
		for i in range(1,n+1):
			re[i] = (re[i-1] and s2[i-1]==s3[i-1])
		for i in range(m):
			for j in range(n+1):
				if j==0:
					re[0]=(re[0] and s1[i]==s3[i])
				else:
					val = False
					if s1[i]==s3[i+j]:
						val |= re[j]
					if s2[j-1]==s3[i+j]:
						val|=re[j-1]
					re[j]=val
		return re[n]
