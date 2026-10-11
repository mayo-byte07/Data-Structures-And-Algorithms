class Solution(object):
    def findMaxAverage(self, nums, k):
        current_sum = 0
        for i in range(k):
            current_sum += nums[i]
        max_sum = current_sum
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            if current_sum > max_sum:
                max_sum = current_sum
        return float(max_sum) / k