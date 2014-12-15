class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        if len(ratings)==0:
            return 0
        re=[0 for i in range(len(ratings))]
        re[0]=1
        for i in range(1,len(ratings),1):
            if ratings[i]>ratings[i-1]:
                re[i]=re[i-1]+1
            else:
                re[i]=1
        sum=re[len(ratings)-1]
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1] and re[i]<=re[i+1]:
                re[i]=re[i+1]+1
            sum+=re[i]
        return sum
        
