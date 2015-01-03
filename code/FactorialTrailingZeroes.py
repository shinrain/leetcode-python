class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        if n<5:
            return 0
        re=0
        while n>0:
            n/=5
            re+=n
        return re
        
