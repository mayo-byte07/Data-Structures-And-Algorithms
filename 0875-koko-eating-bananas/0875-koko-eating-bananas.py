class Solution(object):
    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)
        
        while low < high:
            mid = low + (high - low) // 2
            total_hours = sum((p + mid - 1) // mid for p in piles)
            
            if total_hours <= h:
                high = mid
            else:
                low = mid + 1
                
        return low