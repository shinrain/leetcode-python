class Solution:

	def getPermutation(self, n, k):
		if n==0 or k==0:
			return ""

		num=[i for i in range(1,n+1)]
		t=math.factorial(n-1)
		k-=1
		re=""
		for i in range(n-1,0,-1):
			p=k/t
			re+=str(num[p])
			num.remove(num[p])
			k%=t
			t=t/i
		re+=str(num[0])
		return re
