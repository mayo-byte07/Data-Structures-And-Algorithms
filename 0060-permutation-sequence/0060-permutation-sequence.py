class Solution(object):
    def getPermutation(self, n, k):
        fact = [1] * n
        for i in range(1, n):
            fact[i] = fact[i - 1] * i

        nums = [str(i) for i in range(1, n + 1)]
        k -= 1 
        ans = []

        for i in range(n - 1, -1, -1):
            idx = k // fact[i]
            k %= fact[i]
            ans.append(nums.pop(idx))

        return "".join(ans)