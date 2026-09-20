class Solution(object):
    def reverseDegree(self, s):
        total = 0
        
        # enumerate(s, 1) automatically starts the index 'i' at 1
        for i, char in enumerate(s, 1):
            reversed_val = 123 - ord(char)
            total += reversed_val * i
            
        return total