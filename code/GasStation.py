
class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        n=len(gas)
        if n==0:
            return 0
        diff=[gas[i]-cost[i] for i in range(n)]
        G=[0 for i in range(n)]
        [sum, MIN] = [0, diff[0]]
        for i in range(n):
            sum+=diff[i]
            MIN=min(MIN, sum)
        if MIN>=0:
            return 0
        G[0]=MIN
        for i in range(1,n,1):
            G[i]=min(sum,G[i-1]-diff[i-1])
            if G[i]>=0:
                return i
        return -1
        
