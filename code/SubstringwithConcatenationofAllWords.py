class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
	def findSubstring(self, S, L):
		[m,n]=[len(S), len(L)]
		if m==0:
			return []
		if n==0:
			return [0]
		map={}
		for i in L:
			if i in map:
				map[i]+=1
			else:
				map[i]=1
		l=len(L[0])
		re=[]
		for i in range(0,m):
			if check(S[i:i+n*l], copy.deepcopy(map),l):
				re.append(i)
		return re

def check(s, map,l):
	m=len(map)
	for i in range(0,len(s),l):
		if s[i:i+l] in map:
			if map[s[i:i+l]] ==0:
				return False
			map[s[i:i+l]]-=1
			if map[s[i:i+l]]==0:
				m-=1
			if m<0:
				return False
		else:
			return False
	return m==0
    
