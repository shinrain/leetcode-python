
class Solution:
	# @param strs, a list of strings
	# @return a list of strings
	def anagrams(self, strs):
		n=len(strs)
		if n==0:
			return []
		re=[]
		map={}
		add=[]
		for s in strs:
			l=list(s)
			l.sort()
			key=hash(str(l))
			if key in map:
				re.append(s)
				if map[key] not in add:
					add.append(map[key])
					re.append(map[key])
			else:
				map[key]=s
		return re
