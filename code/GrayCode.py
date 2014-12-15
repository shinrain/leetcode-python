class Solution:
    # @return a list of integers
	def grayCode(self, n):
		re=[]
		for i in range(0, (1<<n)):
			re.append(i^(i>>1))
		return re
        
