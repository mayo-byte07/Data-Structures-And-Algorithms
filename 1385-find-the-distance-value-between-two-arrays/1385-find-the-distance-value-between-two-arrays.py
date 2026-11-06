import bisect

class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        arr2.sort()
        count = 0
        n2 = len(arr2)
        
        for x in arr1:
            idx = bisect.bisect_left(arr2, x - d)
            
            if idx < n2 and arr2[idx] <= x + d:
                continue
                
            count += 1
            
        return count