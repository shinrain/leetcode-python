class Solution:
	# @param x, an integer
	# @return an integer
	def sqrt(self, x):
		if x<0:
			return -1
		if x<=1:
			return x
		[l,r]=[1,x]
		re=-1
		while l<=r:
			mid=l+(r-l)/2
			dif=x/mid
			if dif==mid:
				return mid
			elif dif<mid:

				r=mid-1
			else:
				re=mid
				l=mid+1
		return re
