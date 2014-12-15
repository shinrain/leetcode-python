class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        n=len(s)
        if n==0:
            return True
        
        [l,r]=[0,n-1]
        while l<r:
            [a,b]=[check(s[l]), check(s[r])]
            if a=='.':
                l+=1
            elif b=='.':
                r-=1
            else:
                if a==b:
                    l+=1
                    r-=1
                else:
                    return False
        return True

def check(s):
    s=ord(s)
    if s>=ord('a') and s<=ord('z'):
        return chr(s)
    if s>=ord('A') and s<=ord('Z'):
        return chr(s-ord('A')+ord('a'))
    if s>=ord('0') and s<=ord('9'):
        return chr(s)
    return '.'
