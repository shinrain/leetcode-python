class Solution:
    # @return an integer
    def atoi(self, str):
        str=str.strip()
        n=len(str)
        if n==0:
            return 0
        flg=False
        MAX=(1<<31)-1
        MIN=-(1<<31)
        if str[0]=='+' or str[0]=='-':
            flg=(str[0]=='-')
            str=str[1::]
        re=0
        for i in range(len(str)):
            val = ord(str[i])
            if val>=ord("0") and val<=ord("9"):
                re=re*10+int(str[i])
            else:
                break
        if flg:
            if -re<MIN:
                return MIN
            return -re
        if re>MAX:
            return MAX
        return re
            
