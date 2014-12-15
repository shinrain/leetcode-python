class Solution:
    # @param tokens, a list of string
    # @return an integer
	def evalRPN(self, tokens):
		st=[]
		try:
			for s in tokens:
				if s=="+":
					st.append(st.pop()+st.pop())
				elif s=="-":
					st.append(-st.pop()+st.pop())
				elif s=="*":
					st.append(st.pop()*st.pop())
				elif s=="/":
					a=st.pop()
					b=st.pop()
					if(a*b<0):
						st.append(-(abs(b)/abs(a)))
					else:
						st.append(b/a)
				else:
					st.append(int(s))
				
		except:
			return 0
		return st[0]
                
        
