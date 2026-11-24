import math

class Solution(object):
    def pivotInteger(self, n):
        total_sum = n * (n + 1) // 2
        x = int(math.sqrt(total_sum))
        
        return x if x * x == total_sum else -1