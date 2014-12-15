class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        n=len(candidates)
        if n==0:
            return []
        re=[]
        candidates.sort()
        helper(candidates,0,target,[],re)
        return re

def helper(a,k,target,r,re):
    if k==len(a):
        if target==0:
            re.append(copy.deepcopy(r))
    else:
        val=a[k]
        helper(a,k+1,target,r,re)
        siz=len(r)
        while target-val>=0:
            target-=val
            r.append(val)
            helper(a,k+1,target,r,re)
        for i in range(len(r)-1,siz-1,-1):
            r.remove(r[i])
