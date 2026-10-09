class Solution(object):
    def minInsertions(self, s):
        insertions = 0
        req_close = 0
        for char in s:
            if char == '(':
                if req_close % 2 != 0:
                    insertions += 1
                    req_close -= 1
                    
                req_close += 2
            else:
                req_close -= 1
                if req_close < 0:
                    insertions += 1
                    req_close = 1
        return insertions + req_close