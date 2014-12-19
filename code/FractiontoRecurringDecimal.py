
class Solution:
	# @return a string
	def fractionToDecimal(self, numerator, denominator):
		if numerator==0 or denominator==1:
			return str(numerator)
		if denominator==0:
			return "NaN"
		flg=0
		if numerator<0:
			flg+=1
			numerator=-numerator
		if denominator<0:
			flg+=1
			denominator=-denominator
		re=""
		if numerator%denominator==0:
		    re=str(numerator/denominator)
		elif numerator<denominator:
			re="0."+helper(numerator, denominator)
		elif numerator>denominator:
			re=str(numerator/denominator)+"."+helper(numerator%denominator, denominator)
		else:
			re="1"
		if flg%2==0:
			return re
		else:
			return "-"+re
def helper(a,b):

	re=""
	map={}
	l=[]
	[val, res]=[-1,-1]
	a*=10
	while a!=0:
		if a in map:
			break
		num=a
		sub=""
		while a<b:
			a*=10
			sub+="0"
		res=a%b
		val=sub+str(a/b)
		map[num]=val
		l.append(num)
		a=res*10

	if a==0:
		for ll in l:
		    re+=map[ll]
	else:

		for s in l:
			if s==a:
				re+="("
			re+=map[s]
		re+=")"
	return re
