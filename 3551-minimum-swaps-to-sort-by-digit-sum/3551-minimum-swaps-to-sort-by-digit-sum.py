class Solution(object):
    def minSwaps(self, nums):
        def get_digit_sum(n):
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total
            
        n = len(nums)
        arr = []
        for i in range(n):
            arr.append((get_digit_sum(nums[i]), nums[i], i))
        arr.sort()
        visited = [False] * n
        swaps = 0
        for i in range(n):
            if visited[i] or arr[i][2] == i:
                continue
            cycle_length = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = arr[j][2]
                cycle_length += 1
            if cycle_length > 1:
                swaps += (cycle_length - 1)
                
        return swaps