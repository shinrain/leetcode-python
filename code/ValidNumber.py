
class Solution:
	# @param s, a string
	# @return a boolean
	def isNumber(self, s):
		s=s.strip()
		n=len(s)
		if n==0:
			return False
		[num,e,dot,sign]=[False for i in range(4)]
		for i in range(n):
			if s[i]=="+" or s[i]=="-":
				if i!=0 and s[i-1]!="e":
					return False
			elif s[i]=="e":
				if e or not num:
					return False
				e=True
				num=False
			elif s[i]==".":
				if dot or e:
					return False
				dot=True
			else:
				try:
					int(s[i])
					num=True
				except:
					return False
		return num
