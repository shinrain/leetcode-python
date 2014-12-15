class Solution:
	# @param path, a string
	# @return a string
	def simplifyPath(self, path):
		w=path.strip().split("/")
		st=[]

		for s in w:
			if s=="..":
				if len(st)!=0:
					st.pop()
			elif s=="":
				pass
			elif s!=".":
				st.append(s)

		if len(st)==0:
			return "/"
		re=""
		while len(st)!=0:
			re="/"+st.pop()+re
		return re

