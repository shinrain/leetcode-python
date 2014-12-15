class Solution:
	# @param s, a string
	# @return a list of strings
	def restoreIpAddresses(self, s):
		return helper(s,len(s),4,{})

def helper(s, n, k, map):
	re=[]
	if n==0:
		return re
	key = n*len(s)+k
	if key in map:
		return map[key]
	if k==1:
		if check(s[0:n]):
			re.append(s[0:n])
	else:
		for i in range(n-1,n-4,-1):
			if i <0:
				break
			if check(s[i:n]):
				rr = helper(s,i,k-1,map)
				if len(rr)>0:
					for ss in rr:
						re.append(ss+"."+s[i:n])
	map[key]=re
	return re

def check(s):
	n=len(s)
	if n==0 or n>3:
		return False
	try:
		val = int(s)
		if val>=0 and val<=255 and  (n==1 or s[0]!='0'):
			return True
	except:
		pass
	return False
