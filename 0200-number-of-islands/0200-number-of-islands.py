class Solution(object):
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        island_count = 0
        def sink_island(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            sink_island(r + 1, c)
            sink_island(r - 1, c)
            sink_island(r, c + 1)
            sink_island(r, c - 1)
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    island_count += 1
                    sink_island(r, c)
        return island_count