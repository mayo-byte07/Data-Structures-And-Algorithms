class Solution(object):
    def climbStairs(self, n, costs):
        # Dynamic programming array storing min costs for rolling steps
        dp = [0] * 4
        
        for i in range(1, n + 1):
            cost_i = costs[i - 1]
            min_val = float('inf')
            
            # Check valid jumps of length k = 1, 2, 3
            for k in range(1, 4):
                if i - k >= 0:
                    min_val = min(min_val, dp[(i - k) % 4] + k * k)
                    
            dp[i % 4] = min_val + cost_i
            
        return dp[n % 4]