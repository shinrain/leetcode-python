class Solution:
    # @return an integer
    def maxArea(self, height):
        n=len(height)
        if n<=1:
            return 0
        [l,r]=[0,n-1]
        Max=min(height[l],height[r])*(r-l)
        while l<r:
            Max=max(Max, min(height[l],height[r])*(r-l))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return Max
