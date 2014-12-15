
class Solution:
	# @return a list of lists of string
	def solveNQueens(self, n):
		if n==0:
			return []
		re=[]
		r=[0 for i in range(n)]
		helper(n,0,r,re)
		result=[]
		for i in re:
			r=[]
			for j in i:
				s=""
				for k in range(n):
					if k==j:
						s+="Q"
					else:
						s+="."
				r.append(s)
			result.append(r)
		return result

def helper(n,k,r,re):

	if k==n:
		re.append(copy.deepcopy(r))
	else:
		for i in range(n):
			r[k]=i
			if check(r,k):
				helper(n,k+1,r,re)

def check(r,k):
	for i in range(k):
		if r[i]==r[k] or abs(r[i]-r[k])==k-i:
			return False
	return True
