from collections import deque

class Solution(object):
    def predictPartyVictory(self, senate):
        n = len(senate)
        r_queue = deque()
        d_queue = deque()
        for i, char in enumerate(senate):
            if char == 'R':
                r_queue.append(i)
            else:
                d_queue.append(i)
        while r_queue and d_queue:
            r_idx = r_queue.popleft()
            d_idx = d_queue.popleft()
            if r_idx < d_idx:
                r_queue.append(r_idx + n)
            else:
                d_queue.append(d_idx + n)
        return "Radiant" if r_queue else "Dire"