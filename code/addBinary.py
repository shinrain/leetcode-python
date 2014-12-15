class Solution:
	# @param a, a string
	# @param b, a string
	# @return a string
	def addBinary(self, a, b):
		[m,n]=[len(a),len(b)]
		if m==0:
			return b
		if n==0:
			return a
		carry=0
		[i,j]=[m-1,n-1]
		re=""
		while i>=0 or j>=0:
			val = carry
			if i>=0:
				val+=int(a[i])
				i-=1
			if j>=0:
				val+=int(b[j])
				j-=1
			re=str(val%2)+re
			carry=val/2
		if carry!=0:
			re="1"+re
		return re
