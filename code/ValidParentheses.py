class Solution:
    # @return a boolean
    def isValid(self, s):
        n=len(s)
        if n==0:
            return True
        if n%2==1:
            return False
        syb={}
        syb[")"]="("
        syb["}"]="{"
        syb["]"]="["
        st=[]
        for ss in s:
            if len(st)==0 or ss not in syb:
                st.append(ss)
            else:
                if syb[ss]==st[len(st)-1]:
                    st.pop()
                else:
                    return False
        return len(st)==0
