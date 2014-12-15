class MinStack:
	# @param x, an integer
	# @return an integer

	
	def __init__(self):
		self.size=0
		self.st=[]
		self.minst=[]

	def push(self, x):
		self.st.append(x)
		if self.size==0 or x<=self.minst[len(self.minst)-1]:
			self.minst.append(x)
		self.size+=1



	# @return nothing
	def pop(self):
		if(self.size!=0):
			x = self.st.pop()
			if(self.minst[len(self.minst)-1]==x):
				self.minst.pop()
			self.size-=1

	# @return an integer
	def top(self):
		if(self.size!=0):
			return self.st[self.size-1]
		

	# @return an integer
	def getMin(self):
		if(len(self.minst)!=0):
			return self.minst[len(self.minst)-1]
