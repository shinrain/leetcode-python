class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        n=len(num)
        if n<=1:
            return []
        map={}
        for i in range(n):
            val=num[i]
            if target-val in map:
                return [map[target-val], i+1]
            else:
                map[val]=i+1
        return []
