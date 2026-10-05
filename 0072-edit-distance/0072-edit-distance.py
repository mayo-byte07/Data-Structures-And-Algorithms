class Solution(object):
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        if m < n:
            word1, word2 = word2, word1
            m, n = n, m
        dp = list(range(n + 1))
        for i in range(1, m + 1):
            prev_diag = dp[0]
            dp[0] = i
            for j in range(1, n + 1):
                temp = dp[j]
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = prev_diag
                else:
                    dp[j] = 1 + min(prev_diag, dp[j], dp[j - 1])

                prev_diag = temp
        return dp[n]