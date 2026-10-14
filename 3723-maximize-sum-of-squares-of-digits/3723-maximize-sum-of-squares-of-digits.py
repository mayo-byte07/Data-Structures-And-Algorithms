class Solution(object):
    def maxSumOfSquares(self, num, sum):
        if sum > num * 9:
            return ""
        q = sum // 9
        r = sum % 9
        zeros = num - q - (1 if r > 0 else 0)
        ans = "9" * q
        if r > 0:
            ans += str(r)
        ans += "0" * zeros
        return ans