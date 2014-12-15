class Solution:
    # @return an integer
    def reverse(self, x):
        if x>-10 and x<10:
            return x
        flg=(x<0)
        x=abs(x)
        re=0
        [MIN, MAX]=[-(1<<31), (1<<31)-1]
        while x!=0:
            re=re*10+x%10
            x/=10
        if flg:
            if -re<MIN:
                return 0
            return -re
        else:
            if re>MAX:
                return 0
            return re
