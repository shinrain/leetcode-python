def printMatrix(board):
	for i in board:
		for j in i:
			print(str(j)),
		print
	print 
class Solution:
	# @param board, a 2D array
	# Capture all regions by modifying the input board in-place.
	# Do not return any value.


	def solve(self, board):

		if len(board)==0 or len(board[0])==0:
			return
		for i in range(len(board[0])):
			if board[0][i]=='O':
				board[0][i]='D'
				self.dfs(board, 0, i)
			if board[len(board)-1][i]=='O':
				board[len(board)-1][i]='D'
				self.dfs(board, len(board)-1, i)
		for i in range(len(board)):
			if board[i][0]=='O':
				board[i][0]='D'
				self.dfs(board, i, 0)
			if board[i][len(board[0])-1]=='O':
				board[i][len(board[0])-1]='D'
				self.dfs(board, i, len(board[0])-1)

		printMatrix(board)

		for i in range(len(board)):
			for j in range(len(board[0])):
				if board[i][j]=='D':
					board[i][j]='O'
				else:
					board[i][j]='X'
	def dfs(self, board, i, j):
		st=[]
		st.append((i,j))
		while len(st)!=0:
			ii,jj=st.pop()
			if self.check(board, ii+1, jj):
				st.append((ii+1, jj))
			if self.check(board, ii-1, jj):
				st.append((ii-1, jj))
			if self.check(board, ii, jj+1):
				st.append((ii, jj+1))
			if self.check(board, ii, jj-1):
				st.append((ii, jj-1))

	def check(self, board, i, j):
		if i<0 or i>= len(board) or j<0 or j>=len(board[0]) or board[i][j]!='O':
			return False
		board[i][j]='D'
		return True
