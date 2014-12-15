class Solution:
	# @return a string
	def intToRoman(self, num):
		map=["M","D","C","L","X","V","I"]
		div=1000
		re=""
		for i in range(0,len(map),2):
			val=num/div
			if val<=3:
				for j in range(val):
					re+=map[i]
			elif val==4:
				re+=map[i]
				re+=map[i-1]
			elif val==5:
				re+=map[i-1]
			elif val<9:
				re+=map[i-1]
				for j in range(5,val):
					re+=map[i]
			elif val==9:
				re+=map[i]
				re+=map[i-2]
			num=num%div
			div/=10
		return re
		
