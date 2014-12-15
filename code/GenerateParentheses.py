class Solution:
	# @param an integer
	# @return a list of string
	def generateParenthesis(self, n):
		if n==0:
			return []
		re=[]
		r=["." for i in range(2*n)]
		helper(2*n, 0, 0, r, re)
		return re

def helper(n, k, m, r, re):
	if k==n:
		if m==0:
			re.append("".join(r))
	else:
		if m>0:
			r[k]=")"
			helper(n,k+1,m-1,r,re)
		r[k]="("
		helper(n,k+1,m+1,r,re)
