import heapq

class Solution(object):
    def assignTasks(self, servers, tasks):
        free_servers = [(servers[i], i) for i in range(len(servers))]
        heapq.heapify(free_servers)
        busy_servers = []
        
        ans = []
        curr_time = 0
        
        for j in range(len(tasks)):
            curr_time = max(curr_time, j)
            if not free_servers:
                curr_time = busy_servers[0][0]
            while busy_servers and busy_servers[0][0] <= curr_time:
                free_time, weight, idx = heapq.heappop(busy_servers)
                heapq.heappush(free_servers, (weight, idx))
            weight, idx = heapq.heappop(free_servers)
            ans.append(idx)
            heapq.heappush(busy_servers, (curr_time + tasks[j], weight, idx))
            
        return ans