import collections

class Solution(object):
    def findSubtreeSizes(self, parent, s):
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)

        # 1. Compute BFS order of the original tree (strictly non-decreasing by depth)
        bfs_order = []
        queue = collections.deque([0])
        while queue:
            u = queue.popleft()
            bfs_order.append(u)
            for v in adj[u]:
                queue.append(v)

        # 2. Iterative DFS to find the closest ancestor with matching character
        last_seen = [-1] * 26
        new_parent = list(parent)
        # Stack entries: (node, prev_ancestor) where None marks entry and int marks exit
        stack = [(0, None)]

        while stack:
            u, prev = stack.pop()
            c = ord(s[u]) - 97
            if prev is None:
                old_val = last_seen[c]
                if old_val != -1:
                    new_parent[u] = old_val
                last_seen[c] = u
                stack.append((u, old_val))
                for v in adj[u]:
                    stack.append((v, None))
            else:
                last_seen[c] = prev

        # 3. Aggregate subtree sizes in reverse original depth order
        ans = [1] * n
        for i in range(n - 1, 0, -1):
            u = bfs_order[i]
            ans[new_parent[u]] += ans[u]

        return ans