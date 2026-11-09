import heapq
from sortedcontainers import SortedList

class Solution(object):
    def busiestServers(self, k, arrival, load):
        available = SortedList(range(k))
        busy = []
        count = [0] * k
        
        for i in range(len(arrival)):
            arr_time = arrival[i]
            duration = load[i]
            while busy and busy[0][0] <= arr_time:
                _, server_id = heapq.heappop(busy)
                available.add(server_id)
            if not available:
                continue
            target = i % k
            idx = available.bisect_left(target)
            if idx == len(available):
                idx = 0
                
            assigned_server = available[idx]
            available.remove(assigned_server)
            count[assigned_server] += 1
            heapq.heappush(busy, (arr_time + duration, assigned_server))
        max_requests = max(count)
        return [s for s in range(k) if count[s] == max_requests]