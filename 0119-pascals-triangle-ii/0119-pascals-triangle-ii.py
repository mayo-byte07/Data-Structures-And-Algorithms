class Solution(object):
    def getRow(self, rowIndex):
        # Initialize the result array with 1s to satisfy the required space O(rowIndex)
        row = [1] * (rowIndex + 1)
        
        # Calculate each value dynamically based on the previous value
        for i in range(1, rowIndex):
            row[i] = row[i - 1] * (rowIndex - i + 1) // i
            
        return row