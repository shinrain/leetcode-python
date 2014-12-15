	def longestConsecutive(self, num):
		n=len(num)
		if n==0:
			return 0
		map=set(num)

		res = 0
		cp_map=copy.deepcopy(map)
		for i in map:
			if i not in cp_map:
				continue
			local =1
			t=i-1
			while t in cp_map:
				local+=1
				cp_map.remove(t)
				t-=1
			t=i+1
			while t in cp_map:
				local+=1
				cp_map.remove(t)
				t+=1
			res=max(res,local)
		return res
