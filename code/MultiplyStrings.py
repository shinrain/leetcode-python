class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        [m,n]=[len(num1), len(num2)]
        if m==0:
            return num2
        if n==0:
            return num1
        re=[]
        carry=0
        a=list(num1)
        b=list(num2)
        a.reverse()
        b.reverse()
        for i in range(m+n):
            val=carry
            for j in range(min(i+1, m)):
                k=i-j
                if k<0 or k>=n:
                    continue
                val+=(int(a[j])*int(b[k]))
            re.append(str(val%10))
            carry=val/10
        if carry!=0:
            re.append(str(carry))
        i=m+n-1
        while i>=0 and re[i]=="0":
            i-=1
        if i<0:
            return "0"
        re=re[0:i+1]
        re.reverse()
        return "".join(re)
                
        
