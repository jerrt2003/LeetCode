class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(2, n+1):
            while n%i == 0:
                res += i
                n = n/i
        return res

n = 81
sol = Solution()
print sol.minSteps(n)