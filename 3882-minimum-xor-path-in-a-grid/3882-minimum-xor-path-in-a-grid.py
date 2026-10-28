class Solution(object):
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [set() for _ in range(n)]
        dp[0].add(grid[0][0])
        for j in range(1, n):
            for val in dp[j - 1]:
                dp[j].add(val ^ grid[0][j])
        for i in range(1, m):
            curr_dp = [set() for _ in range(n)]
            for val in dp[0]:
                curr_dp[0].add(val ^ grid[i][0])
            for j in range(1, n):
                for val in dp[j]:
                    curr_dp[j].add(val ^ grid[i][j])
                for val in curr_dp[j - 1]:
                    curr_dp[j].add(val ^ grid[i][j])
            dp = curr_dp
        return min(dp[-1])