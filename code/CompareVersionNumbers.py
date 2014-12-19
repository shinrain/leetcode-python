class Solution:
    # @param a, a string
    # @param b, a string
    # @return a boolean
	def compareVersion(self, version1, version2):
		[a,b]=[-1,-1]
		try:
			a=version1.index(".")
		except:
			pass
		try:
			b=version2.index(".")
		except:
			pass

		[num1, num2]=[0,0]
		if a!=-1:
			num1=int(version1[0:a])
		else:
			num1=int(version1)
		if b!=-1:
			num2=int(version2[0:b])
		else:
			num2=int(version2)

		if num1<num2:
			return -1
		elif num1>num2:
			return 1
		else:
			[v1,v2]=["0","0"]
			if a!=-1:
				v1=version1[a+1::]
			if b!=-1:
				v2=version2[b+1::]
			if v1==v2:
				return 0
			return self.compareVersion(v1,v2)
