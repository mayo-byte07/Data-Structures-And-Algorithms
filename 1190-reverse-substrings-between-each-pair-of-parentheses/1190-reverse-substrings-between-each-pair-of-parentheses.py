class Solution(object):
    def reverseParentheses(self, s):
        n = len(s)
        pair = [0] * n
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i
        res = []
        i = 0
        step = 1  
        while i < n:
            if s[i] == '(' or s[i] == ')':
                i = pair[i]
                step = -step
            else:
                res.append(s[i])
            i += step
        return "".join(res)