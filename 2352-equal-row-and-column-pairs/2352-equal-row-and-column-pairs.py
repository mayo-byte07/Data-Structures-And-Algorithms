import collections

class Solution(object):
    def equalPairs(self, grid):
        n = len(grid)
        row_counts = collections.Counter(tuple(row) for row in grid)
        
        ans = 0
        
        for c in range(n):
            col_tuple = tuple(grid[r][c] for r in range(n))
            ans += row_counts[col_tuple]
            
        return ans