class Solution(object):
    def closedIsland(self, grid):
        if not grid or not grid[0]:
            return 0
            
        m, n = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == 1:
                return
            grid[r][c] = 1
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        for c in range(n):
            if grid[0][c] == 0:
                dfs(0, c)
            if grid[m - 1][c] == 0:
                dfs(m - 1, c)
        for r in range(m):
            if grid[r][0] == 0:
                dfs(r, 0)
            if grid[r][n - 1] == 0:
                dfs(r, n - 1)
        closed_count = 0
        for r in range(1, m - 1):
            for c in range(1, n - 1):
                if grid[r][c] == 0:
                    dfs(r, c)
                    closed_count += 1
        return closed_count