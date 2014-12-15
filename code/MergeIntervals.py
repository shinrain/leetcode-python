# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        n=len(intervals)
        if n==0:
            return []
        intervals.sort(key=lambda x:x.start)
        
        re=[]
        for it in intervals:
            if len(re)==0 or it.start>re[len(re)-1].end:
                re.append(it)
            else:
                re[len(re)-1].end=max(re[len(re)-1].end, it.end)
        return re
