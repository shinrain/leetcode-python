#!/usr/bin/python
class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
	def threeSum(self, num):
		re=[]
		num.sort()
		print num
		for i in range(0,len(num)):
			if i!=0 and num[i]==num[i-1]:
				continue
			else:
				k=i+1
				v=len(num)-1
				while k<v:
					if k!=i+1 and num[k]==num[k-1]:
						k+=1
					elif v!=len(num)-1 and num[v]==num[v+1]:
						v-=1
					else:
						sum = num[i]+num[k]+num[v]
						if sum==0:
							re.append([num[i], num[k], num[v]])

							k+=1
							v-=1
						elif sum<0:
							k+=1
						else:
							v-=1
		return re

if __name__=="__main__":
	sol = Solution()
	a=	[7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6]
	print sol.threeSum(a)
