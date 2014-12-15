class Solution:
	# @param start, a string
	# @param end, a string
	# @param dict, a set of string
	# @return an integer
	def ladderLength(self, start, end, dict):
		if start==end:
			return 1
		count = 1
		[a,b] =[set([start]), set([end])]
		d1=copy.deepcopy(dict)
		d2=copy.deepcopy(dict)
		while len(a)!=0 and len(b)!=0:
			if len(a&b)!=0:
				return count
			a=self.explore(a, d1)
			count+=1

			if len(a&b)!=0:
				return count
			b=self.explore(b, d2)
			count+=1
		return count


	def explore(self, words, dict):

		re=set()
		n =len(words)
		if n==0:
			return re

		for s in words:
			cur = list(s);
			for i in range(len(cur)):
				t = cur[i]
				for j in [chr(k) for k in range(ord('a'),ord('z')+1)]:
					cur[i]=j
					str1 = "".join(cur)
					if str1 in  dict:
						re.add(str1)
				cur[i]=t
		dict=dict-re
		return re
