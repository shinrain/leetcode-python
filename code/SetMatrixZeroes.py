
class Solution:
	# @param matrix, a list of lists of integers
	# RETURN NOTHING, MODIFY matrix IN PLACE.
	def setZeroes(self, matrix):
		m=len(matrix)
		if m==0:
			return
		n=len(matrix[0])
		if n==0:
			return
		row =False
		try:
			matrix[0].index(0)
			row=True
		except:
			pass
		col=False
		for i in range(m):
			if matrix[i][0]==0:
				col=True
				break
		for i in range(1,m):
			for j in range(1,n):
				if matrix[i][j]==0:
					matrix[i][0]=matrix[0][j]=0
		for i in range(1,m):
			for j in range(1,n):
				if matrix[i][0]==0 or matrix[0][j]==0:
					matrix[i][j] = 0
		if row:
			for i in range(n):
				matrix[0][i]=0
		if col:
			for i in range(m):
				matrix[i][0]=0
