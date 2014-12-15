class Solution:
	# @param s, a string
	# @return a string
	def reverseWords(self, s):
		s=s.strip()
		n=len(s)
		s=list(s)
		if n==0:
			return ""
		[i,j]=[0,0]
		while j<n:
			while j<n and s[j]==" ":
				j+=1
			if j==n:
				return ""
			if i!=0:
				[s[i], i]=[" ",i+1]
			while j<n and s[j]!=" ":
				[s[i], i, j]=[s[j], i+1, j+1]
		n=i
		s=self.reverse(s,0,n-1)
		[i,j]=[0,0]
		while j<n:
			while j<n and s[j]!=" ":
				j+=1
			s=self.reverse(s, i,j-1)
			if j==n:
				break
			i=j
			s[i]=" "
			[i,j]=[i+1,j+1]
		return "".join(s[0:n])


	def reverse(self, s, l, r):
		while l<r:
			[t,s[l]]=[s[l],s[r]]
			[s[r], l, r]=[t, l+1, r-1]
		return s
