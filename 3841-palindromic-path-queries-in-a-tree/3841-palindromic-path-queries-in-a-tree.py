class Solution(object):
    def palindromePath(self, n, edges, s, queries):
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        LOG = 17
        up = [[0] * LOG for _ in range(n)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        pref_mask = [0] * n
        char_list = list(s)
        stack = [(0, 0, 0)]
        timer = 0
        
        while stack:
            u, p, state = stack.pop()
            
            if state == 0:
                timer += 1
                tin[u] = timer
                depth[u] = depth[p] + 1 if u != p else 0
                up[u][0] = p
                
                for i in range(1, LOG):
                    up[u][i] = up[up[u][i-1]][i-1]
                    
                char_bit = 1 << (ord(char_list[u]) - 97)
                if u == p:
                    pref_mask[u] = char_bit
                else:
                    pref_mask[u] = pref_mask[p] ^ char_bit
                    
                stack.append((u, p, 1))
                
                for v in adj[u]:
                    if v != p:
                        stack.append((v, u, 0))
            else:
                tout[u] = timer
        A = [0] * (n + 2)
        for i in range(n):
            A[tin[i]] = pref_mask[i]
            
        bit = [0] * (n + 2)
        
        def add(idx, val):
            while idx <= n:
                bit[idx] ^= val
                idx += idx & (-idx)
                
        def query(idx):
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & (-idx)
            return res
        for i in range(1, n + 1):
            add(i, A[i] ^ A[i-1])
            
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for i in range(LOG):
                if (diff >> i) & 1:
                    u = up[u][i]
            if u == v:
                return u
            for i in range(LOG - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u = up[u][i]
                    v = up[v][i]
            return up[u][0]
            
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                old_c = char_list[u]
                
                if old_c != c:
                    diff = (1 << (ord(old_c) - 97)) ^ (1 << (ord(c) - 97))
                    char_list[u] = c
                    add(tin[u], diff)
                    add(tout[u] + 1, diff)
            else:
                u = int(parts[1])
                v = int(parts[2])
                lca = get_lca(u, v)
                mask_u = query(tin[u])
                mask_v = query(tin[v])
                mask_lca = 1 << (ord(char_list[lca]) - 97)
                path_mask = mask_u ^ mask_v ^ mask_lca
                
                if path_mask == 0 or (path_mask & (path_mask - 1)) == 0:
                    ans.append(True)
                else:
                    ans.append(False)
        return ans