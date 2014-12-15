class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
	def merge(self, A, m, B, n):
		if n==0:
			return
		if m==0:
			for i in range(n):
				A[i]=B[i]
			return
		[i,j,k] = [m-1,n-1,m+n-1]
		while i>=0 or j>=0:
			if i<0:
				while j>=0:
					A[k]=B[j]
					k-=1
					j-=1
			elif j<0:
				while i>=0:
					A[k]=A[i]
					k-=1
					i-=1
			else:
				A[k]=max(A[i],B[j])
				k-=1
				if A[i]>B[j]:
					i-=1
				else:
					j-=1
		return
        
