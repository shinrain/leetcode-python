class Solution:
	# @param num, a list of integer
	# @return a list of lists of integers
	def permuteUnique(self, num):
		n=len(num)
		if n==0:
			return []
		num.sort()
		re=[copy.deepcopy(num)]
		while helper(num):
			re.append(copy.deepcopy(num))
		return re

def helper(num):
	n=len(num)
	if n==0:
		return False
	i=n-1
	while i>0 and num[i]<=num[i-1]:
		i-=1
	if i==0:
		return False
	j=n-1
	while j>=i and num[j]<=num[i-1]:
		j-=1
	t=num[i-1]
	num[i-1]=num[j]
	num[j]=t
	[l,r]=[i,n-1]
	while l<r:
		t=num[l]
		num[l]=num[r]
		num[r]=t
		l+=1
		r-=1
	return True
