class Solution(object):
    def generate(self, numRows):
        # Base case: if numRows is 0, return an empty list
        if numRows == 0:
            return []
            
        triangle = []
        
        for i in range(numRows):
            # Start each row with entirely 1s. 
            # The length of the row is always i + 1.
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)
            
        return triangle