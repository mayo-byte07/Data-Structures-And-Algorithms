class Solution(object):
    def minMoves(self, nums):
        max_val = max(nums)
        return len(nums) * max_val - sum(nums)