class Solution(object):
    def rearrangeSticks(self, n, k):
        MOD = 1000000007
        dp = [0] * (k + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            limit = i if i < k else k
            for j in range(limit, 0, -1):
                dp[j] = (dp[j - 1] + (i - 1) * dp[j]) % MOD
            dp[0] = 0

        return dp[k]