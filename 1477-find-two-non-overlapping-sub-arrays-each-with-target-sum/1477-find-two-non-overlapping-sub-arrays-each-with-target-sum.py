class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        # best_len_until[i] stores the minimum length of a valid subarray ending at or before index i
        best_len_until = [float('inf')] * n
        ans = float('inf')
        
        left = 0
        current_sum = 0
        
        for right in range(n):
            current_sum += arr[right]
            
            # Shrink the window from the left if the sum exceeds the target
            while current_sum > target and left <= right:
                current_sum -= arr[left]
                left += 1
            
            # If we find a valid subarray
            if current_sum == target:
                current_len = right - left + 1
                
                # If there is a valid subarray that ended strictly before our current 'left' boundary
                if left > 0 and best_len_until[left - 1] != float('inf'):
                    ans = min(ans, current_len + best_len_until[left - 1])
                
                # Record the length of the current valid subarray
                best_len_until[right] = current_len
            
            # Carry forward the minimum length found so far to ensure the array 
            # always holds the absolute minimum valid length up to index 'right'
            if right > 0:
                best_len_until[right] = min(best_len_until[right], best_len_until[right - 1])
                
        return ans if ans != float('inf') else -1