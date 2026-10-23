class Solution(object):
    def uniquePaths(self, m, n):
        total_moves = m + n - 2
        k = min(m - 1, n - 1)
        
        ans = 1
        for i in range(1, k + 1):
            ans = ans * (total_moves - k + i) // i
            
        return ans