class Solution(object):
    def maxSum(self, nums, k):
        MOD = 10**9 + 7
        bit_counts = [0] * 32
        for num in nums:
            for i in range(32):
                if num & (1 << i):
                    bit_counts[i] += 1
        total_sum = 0
        for i in range(k):
            current_num = 0
            for i in range(32):
                if bit_counts[i] > 0:
                    current_num |= (1<<i)
                    bit_counts[i] -= 1
            total_sum = (total_sum + current_num * current_num ) % MOD
        return total_sum