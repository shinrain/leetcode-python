#!/usr/bin/python

import sys
class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        re=sys.maxint
        num.sort()
        for i in range(0,len(num)):
            if i==0 or num[i]!=num[i-1]:
                k=i+1
                v=len(num)-1
                while k<v:
                    if k==i+1 or num[k]!=num[k-1]:
                        if v==len(num)-1 or num[v]!=num[v+1]:
                            sum = num[i]+num[k]+num[v]
                            if sum==target:
                                return target
                            if abs(sum-target)<abs(re-target):
                                re =sum

                            if sum<0:
                                k+=1
                            else:
                                v-=1
                        else:
                            v-=1
                    else:
                        k+=1
        return re

if __name__=="__main__":
    sol = Solution()
    a=	[-1, 2, 1, -4]
    print sol.threeSumClosest(a,1)


