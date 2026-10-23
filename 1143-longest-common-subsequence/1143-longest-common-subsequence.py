class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        if len(text1) < len(text2):
            text1, text2 = text2, text1
            
        m, n = len(text1), len(text2)
        prev_row = [0] * (n + 1)
        
        for i in range(1, m + 1):
            curr_row = [0] * (n + 1)
            
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    curr_row[j] = prev_row[j - 1] + 1
                else:
                    curr_row[j] = max(prev_row[j], curr_row[j - 1])
            prev_row = curr_row
            
        return prev_row[n]