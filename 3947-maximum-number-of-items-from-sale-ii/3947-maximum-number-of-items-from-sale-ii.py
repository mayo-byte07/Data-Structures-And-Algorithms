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

        sorted_items = sorted(items, key=lambda x: x[1])

        rem = budget
        paired_copies = 0
        ans = rem // min_price

        for factor, price in sorted_items:
            if price > 2 * min_price:
                break

            max_free = multiples[factor] - 1
            if max_free <= 0:
                continue

            take = rem // price
            if take > max_free:
                take = max_free

            paired_copies += take
            rem -= take * price
            total = 2 * paired_copies + (rem // min_price)
            if total > ans:
                ans = total

            if take < max_free:
                break

        return ans