class Solution:
    # @return a list of lists of integers
	def generate(self, numRows):
		if numRows==0:
			return []
		result=[]
		re=[1]
		result.append(re)
		if numRows==1:
			return result
		for i in range(2,numRows+1):
			pre = re
			re=[1]
			for j in range(0, len(pre)-1):
				re.append(pre[j]+pre[j+1])
			re.append(1)
			result.append(re)
		return result
