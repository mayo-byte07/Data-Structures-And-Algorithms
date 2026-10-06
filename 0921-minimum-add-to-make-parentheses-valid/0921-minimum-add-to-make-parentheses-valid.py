class Solution(object):
    def minAddToMakeValid(self, s):
        open_needed = 0
        close_needed = 0
        for char in s:
            if char == '(':
                close_needed += 1
            else:
                if close_needed > 0:
                    close_needed -= 1
                else:
                    open_needed += 1
        return open_needed + close_needed