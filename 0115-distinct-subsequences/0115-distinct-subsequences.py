class Solution(object):
    def numDistinct(self, s, t):
        dp = [0] * (len(t) + 1)
        dp[0] = 1
        
        for i in range(len(s)):
            for j in range(len(t) - 1, -1, -1):
                if s[i] == t[j]:
                    dp[j + 1] += dp[j]
                    
        return dp[-1]