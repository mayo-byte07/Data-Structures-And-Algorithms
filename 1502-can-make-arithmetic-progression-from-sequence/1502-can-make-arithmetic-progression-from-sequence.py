class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        n = len(arr)
        min_val = min(arr)
        max_val = max(arr)

        if (max_val - min_val) % (n - 1) != 0:
            return False

        diff = (max_val - min_val) // (n - 1)
        if diff == 0:
            return True

        i = 0
        while i < n:
            if arr[i] == min_val + i * diff:
                i += 1
            elif (arr[i] - min_val) % diff != 0:
                return False
            else:
                j = (arr[i] - min_val) // diff
                if arr[j] == arr[i]:
                    return False
                arr[i], arr[j] = arr[j], arr[i]

        return True