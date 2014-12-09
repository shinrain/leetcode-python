class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        t = [0 for i in range(n + 1)]
        return self.climb(n, t)

    def climb(self, n, t):
        if n == 0:
            return 1
        elif n < 0:
            return 0
        elif t[n] != 0:
            return t[n]
        else:
            t[n] = self.climb(n - 1, t) + self.climb(n - 2, t)
            return t[n]
