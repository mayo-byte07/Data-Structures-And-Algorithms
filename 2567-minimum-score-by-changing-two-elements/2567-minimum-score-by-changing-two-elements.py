class Solution(object):
    def minimizeSum(self, nums):
        s1 = s2 = s3 = float('inf')
        l1 = l2 = l3 = float('-inf')
        
        for x in nums:
            if x <= s1:
                s3 = s2
                s2 = s1
                s1 = x
            elif x <= s2:
                s3 = s2
                s2 = x
            elif x < s3:
                s3 = x
            if x >= l1:
                l3 = l2
                l2 = l1
                l1 = x
            elif x >= l2:
                l3 = l2
                l2 = x
            elif x > l3:
                l3 = x
        return min(l1 - s3, l3 - s1, l2 - s2)