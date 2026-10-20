class Solution(object):
    def sortableIntegers(self, nums):
        n = len(nums)
        S = sorted(nums)
        
        # Find all valid divisors of n
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        if nums == S:
            return sum(divisors)
            
        ans = 0
        for k in divisors:
            possible = True
            for start in range(0, n, k):
                end = start + k
                A_j = nums[start:end]
                S_j = S[start:end]
                
                drops = 0
                drop_idx = -1
                for i in range(k - 1):
                    if A_j[i] > A_j[i+1]:
                        drops += 1
                        drop_idx = i
                        if drops > 1:
                            break
                if drops > 1:
                    possible = False
                    break
                if drops == 0:
                    if A_j != S_j:
                        possible = False
                        break
                else: 
                    if A_j[drop_idx+1:] + A_j[:drop_idx+1] != S_j:
                        possible = False
                        break
            if possible:
                ans += k
                
        return ans