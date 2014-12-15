class Solution:
	def divide(self, dividend, divisor):
		MAX=(1<<31)-1
		MIN=-(1<<31)

		if dividend==0:
			return 0
		if divisor==0:
			return MAX
		if divisor==1:
			return dividend
		flg=0
		if divisor<0:
			divisor=-divisor
			flg+=1
		if dividend<0:
			dividend=-dividend
			flg+=1
		if dividend<divisor:
			return 0
		if dividend==divisor:
			if flg%2==0:
				return 1
			else:
				return -1
		m=1
		res=divisor
		while res<dividend:
			m<<=1
			res<<=1
		if res==dividend:
			if flg%2==0:
				if m>MAX:
					return MAX
				return m
			else:
				if m<MIN:
					return MIN
				return -m
		m>>=1
		res>>=1
		re = m+self.divide(dividend-res, divisor)
		if flg%2==0:

			if re>MAX:
				return MAX
			return re
		else:

			if -re<MIN:
				return MIN
			return -re
