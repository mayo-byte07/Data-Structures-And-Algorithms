class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)
        return [candy + extraCandies >= max_candies for candy in candies]