class Solution(object):
    def targetIndices(self, nums, target):
        less_count = sum(1 for num in nums if num < target)
        target_count = sum(1 for num in nums if num == target)
        
        return [less_count + i for i in range(target_count)]