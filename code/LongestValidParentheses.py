class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        n=len(s)
        if n==0:
            return 0
        valid=[False for i in range(n)]
        st=[]
        for i in range(n):
            if s[i]==")":
                if len(st)!=0 and s[st[len(st)-1]]=="(":
                    valid[st.pop()]=valid[i]=True
                else:
                    st=[]
            else:
                st.append(i)
        re=0
        local=0
        for i in range(n):
            if valid[i]:
                local+=1
            else:
                local=0
            re=max(re, local)
        return re
