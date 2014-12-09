class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
    	n = len(prices)
    	if n<2:
    		return 0
    	_sum = [0]*n
    	_min = prices[0]
    	for i in range(1,n):
			_min = min(prices[i],_min)
			_sum[i] = max(_sum[i-1],prices[i]-_min)

    	result = _sum[n-1]
    	_max = prices[n-1]
    	for i in range(n-2,0,-1):
			_max = max(_max,prices[i])
			local = _max-prices[i]+_sum[i-1]
			result = max(local,result)
    	return result

if __name__=='__main__':
	sol = Solution()
	print sol.maxProfit([2,1,2,0,1])