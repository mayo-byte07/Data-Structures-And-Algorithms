import collections

class Solution(object):
    def countServers(self, n, logs, x, queries):
        # 1. Sort logs by timestamp ascending
        logs.sort(key=lambda item: item[1])
        
        # 2. Pair queries with their original indices and sort by target time
        sorted_queries = sorted(enumerate(queries), key=lambda item: item[1])
        
        ans = [0] * len(queries)
        cnt = collections.defaultdict(int)
        active_servers = 0
        
        left = 0
        right = 0
        num_logs = len(logs)
        
        # 3. Process each query using sliding window over logs
        for orig_idx, q_time in sorted_queries:
            window_start = q_time - x
            
            # Add logs that fall within the upper bound (<= q_time)
            while right < num_logs and logs[right][1] <= q_time:
                server_id = logs[right][0]
                if cnt[server_id] == 0:
                    active_servers += 1
                cnt[server_id] += 1
                right += 1
                
            # Remove logs that drop out of the lower bound (< window_start)
            while left < num_logs and logs[left][1] < window_start:
                server_id = logs[left][0]
                cnt[server_id] -= 1
                if cnt[server_id] == 0:
                    active_servers -= 1
                left += 1
                
            # Number of inactive servers = total servers - active servers in window
            ans[orig_idx] = n - active_servers
            
        return ans