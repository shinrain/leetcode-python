class Solution:
	# @param digits, a list of integer digits
	# @return a list of integer digits
	def plusOne(self, digits):
		n=len(digits)
		if n==0:
			return [1]
		carry=1

		for i in range(n-1,-1,-1):
			Sum=digits[i]+carry
			digits[i]=Sum%10
			carry=Sum/10
		if carry!=0:
			digits.insert(0,carry)
		return digits
