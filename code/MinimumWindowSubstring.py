class Solution:
    # @return a string
	def minWindow(self, S, T):
		m=len(S)
		n=len(T)
		if n==0 or S==T:
			return T
		if m==0:
			return ""
		map={}
		for s in T:
			if s in map:
				map[s]+=1
			else:
				map[s]=1
		siz=len(map)
		[start, end]=[-1,-1]
		[i,j]=[0,0]
		while j<m:
			if siz>0:
				if S[j] in map:
					map[S[j]]-=1
					if map[S[j]]==0:
						siz-=1
			if siz<=0:
				while siz<=0:
					if S[i] in map:
						map[S[i]]+=1
						if map[S[i]]==1:
							siz+=1
					i+=1
				if start==-1 or end-start+1>j-i+2:
					end=j
					start=i-1
			j+=1
		if start==-1:
			return ""
		return S[start:end+1]
        
