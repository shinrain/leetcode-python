class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        if n==0:
            return []
        re=[[0 for i in range(n)] for i in range(n)]
        lay=(n+1)/2
        count=1
        for i in range(lay):
            for j in range(i, n-i):
                re[i][j]=count
                count+=1
            for j in range(i+1,n-i):
                re[j][n-i-1] = count
                count+=1
            for j in range(n-i-2, i-1, -1):
                re[n-i-1][j] = count
                count+=1
            for j in range(n-i-2, i,-1):
                re[j][i]=count
                count+=1
        return re
