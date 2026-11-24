class Solution(object):
    def maxLength(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return (a * b) // gcd(a, b)

        n = len(nums)
        total_lcm = 1
        max_val = 0
        for x in nums:
            total_lcm = lcm(total_lcm, x)
            if x > max_val:
                max_val = x
        max_limit = total_lcm * max_val

        ans = 1
        for i in range(n):
            curr_prod = 1
            curr_gcd = 0
            curr_lcm = 1
            
            for j in range(i, n):
                x = nums[j]
                curr_prod *= x
                curr_gcd = gcd(curr_gcd, x)
                curr_lcm = lcm(curr_lcm, x)
                
                if curr_prod > max_limit:
                    break
                    
                if curr_prod == curr_lcm * curr_gcd:
                    length = j - i + 1
                    if length > ans:
                        ans = length
                        
        return ans