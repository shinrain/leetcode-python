class Solution:
	# @param candidates, a list of integers
	# @param target, integer
	# @return a list of lists of integers
	def combinationSum2(self, candidates, target):
		re=[]
		candidates.sort()
		helper(candidates,0,target,[],re)
		return re

def helper(a, k, target, r, re):
	if k==len(a):
		if target==0:
			re.append(copy.deepcopy(r))
	else:
		val=a[k]
		n=k
		while n<len(a) and a[n]==val:
			n+=1
		helper(a,n,target,r,re)
		siz=len(r)
		for i in range(k,n):
			if target-val<0:
				break
			target-=val
			r.append(val)
			helper(a,n,target,r,re)
		for i in range(len(r)-1,siz-1,-1):
			r.remove(r[i]) 
