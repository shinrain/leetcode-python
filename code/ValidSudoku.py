class Solution:
	# @param board, a 9x9 2D array
	# @return a boolean
	def isValidSudoku(self, board):
		n=9
		row=[0 for i in range(n)]
		col=[0 for i in range(n)]
		sqr=[0 for i in range(n)]

		for i in range(n):
			for j in range(n):
				if board[i][j]=='.':
					continue
				val=int(board[i][j])-1
				if check(row[i],val):
					return False
				set(row,i,val)
				if check(col[j],val):
					return False
				set(col,j,val)
				if check(sqr[i/3*3+j/3],val):
					return False
				set(sqr,i/3*3+j/3,val)
		return True
def set(a, k, i):
	a[k]|=(1<<i)
def check(a,i):
	return (a&(1<<i))!=0
