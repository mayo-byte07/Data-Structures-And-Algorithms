class Solution(object):
    def numOfSubarrays(self, arr):
        MOD = 10**9 + 7
        ans = 0
        
        even_count = 1
        odd_count = 0
        curr_parity = 0
        
        for num in arr:
            curr_parity ^= (num & 1)
            
            if curr_parity == 1:
                ans = (ans + even_count) % MOD
                odd_count += 1
            else:
                ans = (ans + odd_count) % MOD
                even_count += 1
                
        return ans