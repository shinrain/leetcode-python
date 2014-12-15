class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        m=len(matrix)
        if m==0:
            return []
        n=len(matrix[0])
        if n==0:
            return []
        lay=(min(m,n)+1)/2
        count=0
        re=[]
        for i in range(lay):
            for j in range(i,n-i):
                re.append(matrix[i][j])
                count+=1
                if count==m*n:
                    return re
            for j in range(i+1,m-i):
                re.append(matrix[j][n-i-1])
                count+=1
                if count==m*n:
                    return re
            for j in range(n-i-2, i-1, -1):
                re.append(matrix[m-i-1][j])
                count+=1
                if count==m*n:
                    return re
            for j in range(m-i-2, i,-1):
                re.append(matrix[j][i])
                count+=1
                if count==m*n:
                    return re
        return re
