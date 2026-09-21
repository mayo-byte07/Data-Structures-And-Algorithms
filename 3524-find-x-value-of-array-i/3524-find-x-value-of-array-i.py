class Solution(object):
    def resultArray(self, nums, k):
        # ans[x] will store the total number of valid subarrays yielding remainder x
        ans = [0] * k
        # dp[p] will track the number of subarrays ending at the CURRENT index yielding remainder p
        dp = [0] * k
        
        for num in nums:
            val = num % k
            new_dp = [0] * k
            
            # 1. Extend existing subarrays ending at the previous index
            for p in range(k):
                if dp[p] > 0:
                    new_dp[(p * val) % k] += dp[p]
                    
            # 2. Start a fresh subarray consisting of only the current element
            new_dp[val] += 1
            
            # 3. Accumulate results into the global answer and update state
            for x in range(k):
                ans[x] += new_dp[x]
                dp[x] = new_dp[x]
                
        return ans