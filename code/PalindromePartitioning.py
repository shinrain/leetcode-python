

class Solution:
	# @param s, a string
	# @return a list of lists of string
	def partition(self, s):
		n=len(s)
		if n==0:
			return []
		print "pass in "+s[0:n]
		return self.helper(s, n-1, [[0 for i in range(n)] for i in range(n)],{})
		
	def helper(self, s, n, valid, map):
		re=[]

		if n in map:
			return map[n]
		for j in range(n, -1, -1):
			if self.check(s, j, n, valid):
				if j==0:
					re.append([s[j:n+1]])
				else:
					subresult= copy.deepcopy(self.helper(s,j-1,valid,map))
					for ss in subresult:
						ss.append(s[j:n+1])
						re.append(ss)

		map[n]=re
		return re
	
	def check(self, s, l, r, valid):
		if valid[l][r]!=0:
			return valid[l][r]
		else:
			if s[l]==s[r] and (l+1>=r-1 or valid[l+1][r-1]==1):
				valid[l][r] = 1
			else:
				valid[l][r] = -1
		return valid[l][r]==1
                
    
