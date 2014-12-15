class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
	def minimumTotal(self, triangle):
		n=len(triangle)
		if n==0:
			return 0
		pre = triangle[n-1]
		for i in range(n-2,-1,-1):
			cur=triangle[i]
			for j in range(len(cur)):
				cur[j]= cur[j]+min(pre[j],pre[j+1])
			pre=cur
		return pre[0]
		
