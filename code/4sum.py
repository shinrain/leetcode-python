class Solution:
	# @return a list of lists of length 4, [[val1,val2,val3,val4]]
	def fourSum(self, num, target):
		n=len(num)
		if n==0:
			return []
		num.sort()
		re=[]
		for i in range(n):
			if i==0 or num[i]!=num[i-1]:
				for j in range(i+1,n):
					if j==i+1 or num[j]!=num[j-1]:
						k=j+1
						v=n-1
						while k<v:
							if k!=j+1 and num[k]==num[k-1]:
								k+=1
							elif v!=n-1 and num[v]==num[v+1]:
								v-=1
							else:
								summ=num[i]+num[j]+num[k]+num[v]
								if summ==target:
									re.append([num[i], num[j],num[k], num[v]])
									k+=1
									v-=1
								elif summ<target:
									k+=1
								else:
									v-=1
		return re
