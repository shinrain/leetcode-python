class Solution:
    # @return a string
	def convertToTitle(self, num):
		if num<=0:
			return ""
		re=""
		while num>0:
			num-=1
			val = num%26
			re=chr(val+ord('A'))+re
			num/=26
		return re
