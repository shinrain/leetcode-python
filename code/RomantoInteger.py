class Solution:
    # @return an integer
    def romanToInt(self, s):
        map={}
        map["M"]=1000
        map["D"]=500
        map["C"]=100
        map["L"]=50
        map["X"]=10
        map["V"]=5
        map["I"]=1
        
        n=len(s)
        if n==0:
            return 0
        re=0
        for i in range(n):
            if i==0:
                re+=map[s[i]]
            else:
                cur=map[s[i]]
                pre=map[s[i-1]]
                if cur>pre:
                    re+=(cur-2*pre)
                else:
                    re+=cur
        return re
        
