class mem:
	def __init__(self, key, value):
		[self.key, self.val, self.pre, self.next]=[key,value, None, None]
	def __str__(self):
		re="("+str(self.key)+", "+str(self.val)+")"
		if self.next==None:
			return re
		else:
			return re+"->"+str(self.next)

class LRUCache:

	# @param capacity, an integer
	def __init__(self, capacity):
		[self.cap, self.size, self.map, self.head, self.tail]=[capacity,0,{},None,None]


	# @return an integer
	def get(self, key):
		if key not in self.map:
			return -1
		m=self.map[key]
		if m==self.head:
			return m.val
		if m==self.tail:
			self.tail=self.tail.pre
			self.tail.next=None
			m.pre=None
			m.next=self.head
			self.head.pre=m
			self.head=m
			return m.val
		m.pre.next=m.next
		m.next.pre=m.pre
		m.pre=None
		m.next=self.head
		self.head.pre=m
		self.head=m
		return m.val

	# @param key, an integer
	# @param value, an integer
	# @return nothing
	def set(self, key, value):

		if key in self.map:
			del self.map[key]
			self.tail.key=key
			self.tail.val=value
			self.map[key]=self.tail
			self.get(key)
		else:
			if self.size<self.cap:
				m=mem(key, value)
				m.next=self.head
				if self.head!=None:
					self.head.pre=m
				if self.tail==None:
					self.tail=m
				self.head=m
				self.map[key]=m
				self.size+=1
			else:
				m=mem(key, value)
				if self.size==1:
					del self.map[self.head.key]
					self.head=self.tail=m
					self.map[key]=m
				else:
					del self.map[self.tail.val]
					self.tail.key=key
					self.tail.val=value
					self.map[key]=self.tail
					self.get(key)
