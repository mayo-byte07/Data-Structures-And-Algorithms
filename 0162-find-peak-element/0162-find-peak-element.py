class Solution(object):
    def findPeakElement(self, nums):
        low = 0
        high = len(nums) - 1
        
        while low < high:
            mid = low + (high - low) // 2
            
            if nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                high = mid
                
        return low