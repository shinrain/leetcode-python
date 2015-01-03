class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        n=len(s)
        if n==0:
            return 0
        re=0
        for i in s:
            if ord(i) not in range(ord('A'),ord('Z')+1):
                return re
            re=re*26+ord(i)-ord('A')+1
        return re
        
