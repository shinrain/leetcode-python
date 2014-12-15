class Solution:
    # @param s, a string
    # @param dict, a set of string
	def wordBreak(self, s, dict):
		re=[]
		map={}
		n=len(s)
		if n==0:
			return re
		return self.helper(s,dict, map)

		
	def helper(self, s, dict, map):
		n=len(s)
		re =[]
		if n==0:
			return re
		if n in map:
			return map[n]
		for j in range(n-1, -1,-1):
			if s[j::] in dict:
				if j==0:
					re.append(s)
				else:
					rr=self.helper(s[0:j], dict, map)
					for r in rr:
						re.append(r+" "+s[j::])
		map[n]=re
		return re
