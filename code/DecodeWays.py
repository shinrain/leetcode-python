class Solution:
    # @param s, a string
    # @return an integer
	def numDecodings(self, s):
		n=len(s)
		if n==0:
			return 0
		re=[0 for i in range(n)]
		for i in range(n):
			for j in range(i, i-2,-1):
				if j<0:
					break
				if check(s[j:i+1]):
					if j==0:
						re[i]+=1
					else:
						re[i]+=re[j-1]
		return re[n-1]

def check(s):
	n=len(s)
	if n==0 or n>=3 or s[0]=='0':
		return False
	try:
		val =int(s)
		if val in range(1,27):
			return True
	except:
		pass
	return False
        
