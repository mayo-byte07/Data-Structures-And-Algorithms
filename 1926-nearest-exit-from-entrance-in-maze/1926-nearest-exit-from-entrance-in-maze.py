from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        m, n = len(maze), len(maze[0])
        start_r, start_c = entrance
        queue = deque([(start_r, start_c, 0)])
        maze[start_r][start_c] = '+'
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            r, c, steps = queue.popleft()
            if (r != start_r or c != start_c) and (r == 0 or r == m - 1 or c == 0 or c == n - 1):
                return steps
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == '.':
                    maze[nr][nc] = '+'
                    queue.append((nr, nc, steps + 1))
        return -1