class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        best_len_until = [float('inf')] * n
        ans = float('inf')
        left = 0
        current_sum = 0
        for right in range(n):
            current_sum += arr[right]
            while current_sum > target and left <= right:
                current_sum -= arr[left]
                left += 1
            if current_sum == target:
                current_len = right - left + 1
                if left > 0 and best_len_until[left - 1] != float('inf'):
                    ans = min(ans, current_len + best_len_until[left - 1])
                best_len_until[right] = current_len
            if right > 0:
                best_len_until[right] = min(best_len_until[right], best_len_until[right - 1])
                
        return ans if ans != float('inf') else -1