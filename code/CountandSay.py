class Solution:
    # @return a string
    def countAndSay(self, n):
    	if n==0:
    		return ""
    	re = ["1"]
    	for i in range(n-1):
    		val = re[0]
    		cnt = 0
    		r = []
    		for j in re:
    			if j==val:
    				cnt+=1
    			else:
    				r.append(str(cnt))
    				r.append(str(val))
    				cnt = 1
    				val = j
    		r.append(str(cnt))
    		r.append(str(val))
    		re = r

    	return ''.join(re)

if __name__=="__main__":
	solution = Solution()
	for i in range(5):
		print str(i)+": "+solution.countAndSay(i)
