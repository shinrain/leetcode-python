    def addBinary(self, a, b):
        m=len(a)
        n=len(b)
        if(m==0):
            return b
        if(n==0):
            return a
        
        re=""
        i=m-1
        j=n-1
        
        carry = 0
        while i>=0 or j>=0:
            if j<0:
                sum = ord(a[i])-ord('0')+carry
            elif i<0:
                sum = ord(b[j]) - ord('0')+carry
            else:
                sum = ord(a[i])+ord(b[j])-2*ord('0')+carry
            re = (str)(sum%2)+re
            carry=sum/2
            i-=1
            j-=1

        if carry!=0:
            re = "1"+re
        return re
