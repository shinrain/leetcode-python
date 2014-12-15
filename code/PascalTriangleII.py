	def getRow(self, rowIndex):
		if rowIndex==0:
			return [1]
		cur = [1,1]
		if rowIndex==1:
			return cur
		for i in range(2,rowIndex+1):
			pre = cur
			cur=[1]
			for j in range(len(pre)-1):
				cur.append(pre[j]+pre[j+1])
			cur.append(1)
		return cur
