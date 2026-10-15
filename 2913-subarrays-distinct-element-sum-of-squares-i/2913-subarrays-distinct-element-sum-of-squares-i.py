class Solution(object):
    def sumCounts(self, nums):
        total_sum = 0
        n = len(nums)
        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(nums[j])
                distinct_count = len(seen)
                total_sum += distinct_count * distinct_count
        return total_sum