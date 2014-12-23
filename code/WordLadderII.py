class Solution:
    # @param num, a list of integer
    # @return an integer
	def findLadders(self, start, end, dict):
		if start==end:
			return [[start]]
		dict.add(start)
		dict.add(end)

		dict1=copy.deepcopy(dict)
		dict2=copy.deepcopy(dict)
		dict1.remove(start)
		dict2.remove(end)
		l1=set([start])
		l2=set([end])

		map1={}
		map2={}
		inter=set()
		while l1 and l2:
			l1=explore(l1, dict1, map1)

			inter=l1 & l2

			if inter:
				break
			l2=explore(l2, dict2, map2)
			inter=l1 & l2

			if inter:
				break
		re=[]

		for s in inter:
			left=recover(map1, s, start)
			right=recover(map2, s, end)

			for ll in left:
				l=[ll[i] for i in range(len(ll)-1,-1,-1)]
				for rr in right:
					if len(rr)==1:
						re.append(l[:])
					else:
						l_cp=l[:]
						for i in range(1,len(rr)):
							l_cp.append(rr[i])
						re.append(l_cp)
		return re

def explore(l, dict, map):
	re=set()
	for i in l:
		cur=list(i)
		for j in range(len(i)):
			t=i[j]
			for letter in range(ord('a'), ord('z')+1):
				if chr(letter)==t:
					continue
				cur[j]=chr(letter)
				curstr="".join(cur)
				if curstr in dict:
					re.add(curstr)
					if curstr not in map:
						map[curstr]=set([i])
					else:
						map[curstr].add(i)
			cur[j]=t
	for i in re:
		dict.remove(i)
	return re

def recover(map, start, end):
	re=[]
	if start==end:
		return [[start]]
	else:

		for s in map[start]:
			ll=recover(map,s,end)
			for l in ll:
				l.insert(0,start)
				re.append(l)
	return re

