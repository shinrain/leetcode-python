
class Solution:
	# @param intervals, a list of Intervals
	# @param newInterval, a Interval
	# @return a list of Interval
	def insert(self, intervals, newInterval):
		n=len(intervals)
		if n==0:
			return [newInterval]

		re=[]
		for i in range(n):
			cur=intervals[i]
			if cur.end<newInterval.start:
				re.append(cur)
			elif cur.start>newInterval.end:
				re.append(newInterval)
				newInterval = cur
			else:
				newInterval.start=min(cur.start, newInterval.start)
				newInterval.end=max(cur.end, newInterval.end)
		re.append(newInterval)
		return re
