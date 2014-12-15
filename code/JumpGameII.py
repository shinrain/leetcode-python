class Solution:
	# @param A, a list of integers
	# @return an integer
	def jump(self, A):
		n=len(A)
		if n==0:
			return -1
		if n==1:
			return 0
		re=0
		[start,end]=[0,0]
		while start<=end:
			Max=0
			for i in range(start, end+1):
				Max=max(Max, A[i]+i)
				if Max>=n-1:
					return re+1
			re+=1
			start=end+1
			end=Max
		return re+1
