class Solution:
    # @param A a list of integers
    # @return an integer
	def removeDuplicates(self, A):
		n=len(A)
		if n==0:
			return 0
		[i,j,val,count]=[0,0,A[0],0]
		while j<n:
			if val ==A[j]:
				count+=1
				if count<=2:
					A[i]=A[j]
					i+=1
			else:
				count=1
				val=A[j]
				A[i]=A[j]
				i+=1
			j+=1
		return i
