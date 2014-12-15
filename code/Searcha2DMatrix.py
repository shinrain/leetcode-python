class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
	def searchMatrix(self, matrix, target):
		m=len(matrix)
		if m==0:
			return False
		n=len(matrix[0])
		if n==0:
			return False
		[l,r, re]=[0,m-1,-1]
		while l<=r:
			mid=l+(r-l)/2
			if matrix[mid][n-1]==target:
				return True
			if matrix[mid][n-1]<target:
				l=mid+1
			else:
				re=mid
				r=mid-1
		if re==-1:
			return False
		[l,r]=[0,n-1]
		while l<=r:
			mid = l+(r-l)/2
			if matrix[re][mid]==target:
				return True
			elif matrix[re][mid]<target:
				l=mid+1
			else:
				r=mid-1
		return False
        
