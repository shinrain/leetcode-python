class Solution:
    # @return a list of lists of integers
	def combine(self, n, k):
		re=[]
		if k==0 or n<k:
			return []
		if n==k:
			re.append([i+1 for i in range(n)])
			return re

		re=self.combine(n-1,k)
		r=self.combine(n-1,k-1)
		if len(r)==0:
			re.append([n])
		for l in r:
			l.append(n)
			re.append(l)
		return re
