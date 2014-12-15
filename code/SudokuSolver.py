class Solution:
	# @param board, a 9x9 2D array
	# Solve the Sudoku by modifying the input board in-place.
	# Do not return any value.
	def solveSudoku(self, board):
		n=len(board)
		if n==0:
			return
		helper(board,0,0)
		

def helper(board, i, j):
	if i==len(board):
		return True
	if j==len(board[0]):
		return helper(board,i+1,0)
	elif board[i][j]!='.':
		return helper(board,i,j+1)
	else:
		for ii in range(1,len(board)+1):
			board[i][j]=str(ii)
			if check(board, i,j):
				if helper(board, i, j+1):
				    return True
			board[i][j]='.'
		return False

def check(board, i, j):
	for ii in range(len(board)):
		if ii!=i and board[ii][j]==board[i][j]:
			return False
	for ii in range(len(board)):
		if ii==j:
			continue
		if board[i][ii]==board[i][j]:
			return False
	a=i/3
	b=j/3
	for ii in range(3):
		for jj in range(3):
			[c,d]=[a*3+ii, b*3+jj]
			if c==i or d==j:
				continue
			if board[c][d]==board[i][j]:
				return False
	return True
