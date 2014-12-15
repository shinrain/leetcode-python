class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
	def maximalRectangle(self, matrix):
		m=len(matrix)
		if m==0:
			return 0
		n=len(matrix[0])
		if n==0:
			return 0
		re=[int(matrix[0][i]) for i in range(n)]
		Max = histogram(re)
		for i in range(1,m):
			for j in range(n):
				if matrix[i][j]=="1":
					re[j]+=1
				else:
					re[j]=0
			Max=max(Max,histogram(re))
		return Max


def histogram(a):
	print a,
	n=len(a)
	if n==0:
		return 0
	st=[]
	Max=0
	i=0
	while i<n:
		if len(st)==0 or a[i]>=a[st[len(st)-1]]:
			st.append(i)
			
		else:
			tmp=a[st.pop()]
			if len(st)==0:
				local = tmp*i
				Max=max(Max, local)
			else:
				local = tmp*(i-st[len(st)-1]-1)
				Max=max(Max, local)

	while len(st)!=0:
		tmp = a[st.pop()]
		if len(st)==0:
			local = tmp*n
			Max=max(Max, local)
		else:
			local = tmp*(n-st[len(st)-1]-1)
			Max=max(Max, local)
	print Max
	return Max
        
