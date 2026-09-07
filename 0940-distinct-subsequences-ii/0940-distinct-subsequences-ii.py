class Solution(object):
    def distinctSubseqII(self, s):
        MOD = 10**9 + 7
        ends_with = [0] * 26
        total_subsequences = 0
        for char in s:
            char_idx = ord(char) - ord('a')
            old_count = ends_with[char_idx]
            ends_with[char_idx] = (total_subsequences + 1) % MOD
            total_subsequences = (total_subsequences + ends_with[char_idx] - old_count) % MOD
            
        return total_subsequences