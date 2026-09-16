import math

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # Calculate (n + k - 1) choose (2 * k)
        total_ways = math.comb(n + k - 1, 2 * k)
        
        return total_ways % MOD