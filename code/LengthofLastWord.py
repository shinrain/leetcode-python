
class Solution:
	# @param s, a string
	# @return an integer
	def lengthOfLastWord(self, s):
		s=s.strip()
		if len(s)==0:
			return 0
		w=s.rsplit()
		return len(w[-1])

