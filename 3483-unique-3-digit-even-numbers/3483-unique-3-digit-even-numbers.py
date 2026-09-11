class Solution:
    def totalNumbers(self, digits):
        freq = [0] * 10
        for digit in digits:
            freq[digit] += 1
        count = 0
        for a in range(1, 10):
            for b in range(10):
                for c in range(0, 10, 2):

                    used = [0] * 10
                    used[a] += 1
                    used[b] += 1
                    used[c] += 1
                    if all(used[d] <= freq[d] for d in range(10)):
                        count += 1
        return count