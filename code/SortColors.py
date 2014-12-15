class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
	def sortColors(self, A):
		n=len(A)
		if n==0:
			return
		[i,j]=[0,n-1]
		while i<n and A[i]==0:
			i+=1
		if i==n:
			return
		while j>=i and A[j]==2:
			j-=1
		if j<i:
			return
		k=i
		while k<=j:
			if A[k]==0:
				t=A[i]
				A[i]=A[k]
				A[k]=t
				i+=1
			elif A[k]==2:
				t=A[j]
				A[j]=A[k]
				A[k]=t
				j-=1
			else:
				k+=1
			if k<i:
				k=i
        
