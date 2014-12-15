class Solution:
	# @param x, a float
	# @param n, a integer
	# @return a float
	def pow(self, x, n):
		if n==0 or x==1:
			return 1
		if n==1:
			return x
		flg=n<0
		n=abs(n)
		half=pow(x,n/2)
		re=half*half
		if n%2==1:
			re*=x
		if flg:
			return 1/re
		else:
			return re
