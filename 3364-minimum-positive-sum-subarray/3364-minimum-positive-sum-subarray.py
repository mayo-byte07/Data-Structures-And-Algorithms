class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        n = len(nums)
        INF = float('inf')
        min_sum = INF
        
        for i in range(n - l + 1):
            curr_sum = 0
            for j in range(i, min(n, i + r)):
                curr_sum += nums[j]
                if j - i + 1 >= l and curr_sum > 0:
                    if curr_sum < min_sum:
                        min_sum = curr_sum
                        
        return min_sum if min_sum != INF else -1