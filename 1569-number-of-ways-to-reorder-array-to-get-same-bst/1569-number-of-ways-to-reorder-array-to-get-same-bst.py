class Solution(object):
    def numOfWays(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        comb = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            comb[i][0] = 1
            for j in range(1, i + 1):
                comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD
                
        def get_ways(arr):
            if len(arr) <= 2:
                return 1
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            left_ways = get_ways(left)
            right_ways = get_ways(right)
            interleave_ways = comb[len(left) + len(right)][len(left)]
            return (interleave_ways * left_ways * right_ways) % MOD
        return (get_ways(nums) - 1 + MOD) % MOD