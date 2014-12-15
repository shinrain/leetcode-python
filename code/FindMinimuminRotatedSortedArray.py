class Solution:
	# @param num, a list of integer
	# @return an integer
	def findMin(self, num):
		n =len(num)
		if n==0:
			return -1
		l=0
		r=n-1
		re=max(num)
		while l<=r:
			mid=l+(r-l)/2
			if num[mid]>num[l]:
				re = min(num[l], re)
				l=mid+1
			elif num[mid]<num[l]:
				re=min(re, num[mid])
				r=mid-1
			else:
				re=min(re,num[l])
				l+=1
		return re
