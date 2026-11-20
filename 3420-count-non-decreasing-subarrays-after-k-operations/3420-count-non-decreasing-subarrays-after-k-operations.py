import collections

class Solution(object):
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)
        dq = collections.deque()
        curr_cost = 0
        ans = 0
        r = n - 1
        
        for l in range(n - 1, -1, -1):
            val = nums[l]
            merged_count = 1
            while dq and dq[0][0] <= val:
                block_val, cnt = dq.popleft()
                curr_cost += (val - block_val) * cnt
                merged_count += cnt
                
            dq.appendleft([val, merged_count])
            while curr_cost > k:
                curr_cost -= dq[-1][0] - nums[r]
                dq[-1][1] -= 1
                if dq[-1][1] == 0:
                    dq.pop()
                r -= 1
                
            ans += r - l + 1
            
        return ans