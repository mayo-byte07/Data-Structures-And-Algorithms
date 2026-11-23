class Solution(object):
    def shuffle(self, nums, n):
        ans = [0] * (2 * n)
        
        for i in range(n):
            ans[2 * i] = nums[i]
            ans[2 * i + 1] = nums[i + n]
            
        return ans