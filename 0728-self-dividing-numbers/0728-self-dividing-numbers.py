class Solution(object):
    def selfDividingNumbers(self, left, right):
        def is_self_dividing(num):
            curr = num
            while curr > 0:
                digit = curr % 10
                if digit == 0 or num % digit != 0:
                    return False
                curr //= 10
            return True

        ans = []
        for num in range(left, right + 1):
            if is_self_dividing(num):
                ans.append(num)
        return ans