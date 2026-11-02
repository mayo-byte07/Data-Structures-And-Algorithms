class Solution(object):
    def numTilings(self, n):
        MOD = 10**9 + 7
        
        if n == 1:
            return 1
        if n == 2:
            return 2
            
        f0, f1, f2 = 1, 1, 2
        
        for _ in range(3, n + 1):
            f3 = (2 * f2 + f0) % MOD
            f0, f1, f2 = f1, f2, f3
            
        return f2