class Solution:
	# @param grid, a list of lists of integers
	# @return an integer
	def minPathSum(self, grid):
		m=len(grid)
		if m==0:
			return 0
		n=len(grid[0])
		if n==0:
			return 0
		re=[grid[0][0]]
		for i in range(1,n):
			re.append(re[i-1]+grid[0][i])


		for i in range(1,m):
			for j in range(n):
				if j==0:
					re[j]+=grid[i][j]
				else:
					re[j]=min(re[j],re[j-1])+grid[i][j]

		return re[n-1]
