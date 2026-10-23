class Solution(object):
    def sortPermutation(self, nums):
        ans =-1
        for i in range(len(nums)):
            if nums[i] !=i:
                if ans == -1:
                    ans = nums[i]
                else:
                    ans &= nums[i]
        if ans == -1:
            return 0
        return ans