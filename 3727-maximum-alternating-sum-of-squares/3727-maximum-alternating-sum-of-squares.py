class Solution(object):
    def maxAlternatingSum(self, nums):
        for i in range(len(nums)):
            nums[i] = nums[i] * nums[i]
        nums.sort(reverse=True)
        k = (len(nums) + 1) // 2
        score = 0
        for i in range(k):
            score += nums[i]
        for i in range(k, len(nums)):
            score -= nums[i]
            
        return score