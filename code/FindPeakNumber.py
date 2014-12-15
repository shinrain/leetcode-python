#!/usr/bin/python

import sys
class Solution:
	# @param num, a list of integer
	# @return an integer
	def findPeakElement(self, num):
		if len(num)==0:
			return -1
		if len(num)==1:
			return 0
		re = -1
		l=0
		r=len(num)-1
		while l<=r:
			mid = l+(r-l)/2
			if mid==0:
				if num[mid]>num[mid+1]:
					return mid
				else:
					re = mid+1
					l=mid+1
			elif mid==len(num)-1:
				if num[mid]>num[mid-1]:
					return mid
				else:
					re=mid-1
					r=mid-1
			elif num[mid]>num[mid-1] and num[mid]>num[mid+1]:
				return mid
			elif num[mid]>num[mid-1]:
				re = mid+1
				l=mid+1
			else:
				re=mid-1
				r=mid-1;
		return re

if __name__=="__main__":
	sol = Solution()
	a=	[1]
	print sol.findPeakElement(a)


