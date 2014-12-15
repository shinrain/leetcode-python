import sys
class Solution:
	# @param A, a list of integers
	# @return an integer
	def maxProduct(self, A):
		n=len(A)
		if n==0:
			return 0
		elif n==1:
			return A[0]
		else:
			[neg, pos, maxNeg, minPos, prod, res] = [False, False, 0, 0, 1, -sys.maxint-1]
			for i in A:
				prod*=i
				res=max(res, prod)
				if prod>0:
					if not pos or prod<minPos:
						pos=True
						minPos = prod
					else:
						res=max(res, prod/minPos)
				elif prod<0:
					if not neg or prod>maxNeg:
						neg=True
						maxNeg = prod
					else:
						res=max(res,prod/maxNeg)
				else:
					[prod, neg, pos] =[1, False, False]
		return res
