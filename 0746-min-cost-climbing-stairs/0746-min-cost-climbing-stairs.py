class Solution(object):
    def minCostClimbingStairs(self, cost):
        first = cost[0]
        second = cost[1]
        
        for i in range(2, len(cost)):
            first, second = second, cost[i] + min(first, second)
        return min(first, second)