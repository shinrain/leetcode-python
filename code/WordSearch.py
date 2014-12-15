class Solution:
	# @param board, a list of lists of 1 length string
	# @param word, a string
	# @return a boolean
	def exist(self, board, word):
		if len(word)==0:
			return True
		m=len(board)
		if m==0:
			return False
		n=len(board[0])
		if n==0:
			return False

		for i in range(m):
			for j in range(n):
				if board[i][j]==word[0]:
					visit=[[False for ii in range(n)] for ii in range(m)]
					visit[i][j]=True
					if dfs(board, i, j, word[1::], visit):
						return True
		return False

def dfs(board, i, j, word, visit):
	if len(word)==0:
		return True
	if check(board, i+1,j,word,visit):
		if dfs(board, i+1, j, word[1::], visit):
			return True
		visit[i+1][j] = False

	if check(board,i-1,j,word,visit):
		if dfs(board, i-1, j, word[1::], visit):
			
			return True
		visit[i-1][j]=False

	if check(board,i,j+1,word,visit):
		if dfs(board, i, j+1, word[1::], visit):
			
			return True
		visit[i][j+1]=False

	if check(board,i,j-1,word,visit):
		if dfs(board, i, j-1, word[1::], visit):
			
			return True
		visit[i][j-1]=False
	return False

def check(board, i, j, word, visit):

	if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or visit[i][j] or board[i][j]!=word[0]:
		return False

	visit[i][j]=True
	return True
