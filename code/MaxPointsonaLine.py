# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
	def maxPoints(self, points):
		n=len(points)
		if n<=2:
			return n

		res=0
		for i in range(0,n):
			cur = points[i]
			local=0
			map={}
			[vertical, overlap]=[0,0]
			for j in range(i+1, n):
				cmp=points[j]
				[dx, dy] = [cur.x-cmp.x, cur.y-cmp.y]
				if dx==0:
					if dy==0:
						overlap+=1
					else:
						vertical+=1
						local=max(local, vertical);
				elif dy==0:
					if 0.0 in map:
						map[0.0]+=1;
					else:
						map[0.0]=1;
					local=max(map[0.0],local)
				else:
					k=(float)(dy)/dx
					if k in map:
						map[k]+=1
					else:
						map[k]=1
					local=max(local, map[k])

			res=max(local+overlap+1, res)
		return res
        
