class Solution(object):
    def maximumSaleItems(self, items, budget):
        max_factor = 0
        min_price = float('inf')
        for factor, price in items:
            if factor > max_factor:
                max_factor = factor
            if price < min_price:
                min_price = price

        freq = [0] * (max_factor + 1)
        for factor, _ in items:
            freq[factor] += 1

        multiples = [0] * (max_factor + 1)
        for f in range(1, max_factor + 1):
            if freq[f] > 0:
                for m in range(f, max_factor + 1, f):
                    multiples[f] += freq[m]

        dp = [-1] * (budget + 1)
        dp[0] = 0

        for factor, price in items:
            if price <= budget:
                gain = multiples[factor]
                for w in range(budget, price - 1, -1):
                    if dp[w - price] != -1:
                        val = dp[w - price] + gain
                        if val > dp[w]:
                            dp[w] = val

        ans = 0
        for w in range(budget + 1):
            if dp[w] != -1:
                total = dp[w] + (budget - w) // min_price
                if total > ans:
                    ans = total

        return ans