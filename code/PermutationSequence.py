class Solution:
	# @return a string
	def getPermutation(self, n, k):
		if n==0:
			return ""
		re=""
		for i in range(n):
			re+=str(i+1)
		if k==1:
		    return re
		for i in range(1,k):
			re=perm(re)
		return re

def perm(s):
	s=list(s)
	n=len(s)
	i=n-1
	while i>0 and str(s[i]) <=str(s[i-1]):
		i-=1
	if i==0:
		s.sort()
		return "".join(s)
	j=n-1
	while j>=i and s[j]<=s[i-1]:
		j-=1
	t=s[j]
	s[j]=s[i-1]
	s[i-1]=t
	[l,r]=[i,n-1]
	while l<r:
		t=s[l]
		s[l]=s[r]
		s[r]=t
		l+=1
		r-=1
	return "".join(s)
