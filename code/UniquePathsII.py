class Solution:
	# @param obstacleGrid, a list of lists of integers
	# @return an integer
	def uniquePathsWithObstacles(self, obstacleGrid):
		m=len(obstacleGrid)
		if m==0:
			return 0
		n=len(obstacleGrid[0])
		if n==0:
			return 0
		re=[]
		for i in range(n):
			if obstacleGrid[0][i]==0 and (i==0 or re[i-1]==1):
				re.append(1)
			else:
				re.append(0)
		for i in range(1,m):
			for j in range(n):
				if j==0:
					if obstacleGrid[i][j]==1 or re[j]==0:
						re[j]=0
				else:
					if obstacleGrid[i][j]==1:
						re[j]=0
					else:
						re[j]+=re[j-1]
		return re[n-1]
