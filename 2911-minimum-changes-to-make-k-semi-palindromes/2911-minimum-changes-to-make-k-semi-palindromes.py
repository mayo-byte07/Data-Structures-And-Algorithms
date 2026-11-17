class Solution(object):
    def minimumChanges(self, s, k):
        n = len(s)
        divisors = [[] for _ in range(n + 1)]
        for length in range(2, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divisors[length].append(d)
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                min_changes = length
                for d in divisors[length]:
                    changes = 0
                    for step in range(d):
                        l = i + step
                        r = j - d + 1 + step
                        while l < r:
                            if s[l] != s[r]:
                                changes += 1
                            l += d
                            r -= d
                    if changes < min_changes:
                        min_changes = changes
                cost[i][j] = min_changes
        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[0] = 0
        
        for p in range(1, k + 1):
            next_dp = [INF] * (n + 1)
            for i in range(2 * p, n + 1):
                for j in range(2 * (p - 1), i - 1):
                    val = dp[j] + cost[j][i - 1]
                    if val < next_dp[i]:
                        next_dp[i] = val
            dp = next_dp
            
        return dp[n]