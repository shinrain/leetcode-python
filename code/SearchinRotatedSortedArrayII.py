class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
	def search(self, A, target):
		n = len(A)
		if n==0:
			return False
		[l,r]=[0,n-1]
		while l<=r:
			mid=l+(r-l)/2
			if A[mid]==target:
				return True
			if A[mid]>A[l]:
				if target>=A[l] and target<A[mid]:
					r=mid-1
				else:
					l=mid+1
			elif A[mid]<A[l]:
				if target>A[mid] and target<=A[r]:
					l=mid+1
				else:
					r=mid-1
			else:
				l+=1
		return False
        
