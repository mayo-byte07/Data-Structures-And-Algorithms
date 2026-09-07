from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        if fresh_count == 0:
            return 0
        minutes = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            level_size = len(queue)
            rotted_this_minute = False
            for _ in range(level_size):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2          
                        fresh_count -= 1         
                        queue.append((nr, nc))    
                        rotted_this_minute = True
            if rotted_this_minute:
                minutes += 1
        return minutes if fresh_count == 0 else -1