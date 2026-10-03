class Solution(object):
    def removeStars(self, s):
        stack = []
        
        for char in s:
            if char == '*':
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)