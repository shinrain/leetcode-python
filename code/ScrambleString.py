class Solution:
	# @return a boolean
	def isScramble(self, s1, s2):
		return helper(s1,s2,{})

class pair:
	def __init__(self, s1, s2):
		self.s1=max(s1,s2)
		self.s2=min(s1,s2)
	def __hash__(self):
		return hash(self.s1)*31+hash(self.s2)
	def __eq__(self, other):
		return [self.s1, self.s2] == [other.s1, other.s2]

def helper(s1, s2, map):
	if s1==s2:
		return True
	if len(s1)!=len(s2):
		return False
	p=pair(s1,s2)
	if p in map:
		return map[p]

	for i in range(1,len(s1)):
		if helper(s1[0:i],s2[0:i],map) and helper(s1[i::],s2[i::],map):
			map[p]=True
			return True
		if helper(s1[0:i],s2[len(s1)-i::],map) and helper(s1[i::],s2[0:len(s1)-i],map):
			map[p]=True
			return True
	map[p]=False
	return False
