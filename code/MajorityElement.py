class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        n=len(num)
        if n==0:
            return -1
        val=num[0]
        count=0
        for i in num:
            if val==i:
                count+=1
            else:
                if count==0:
                    val = i
                    count=1
                else:
                    count-=1
        count=0
        for i in num:
            if val==i:
                count+=1
        if count>=n/2:
            return val
        return -1
