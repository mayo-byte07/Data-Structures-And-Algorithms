class Solution(object):
    def createGrid(self, m, n):
        grid = []
        
        for i in range(m):
            if i == 0:
                grid.append("." * n)
            else:
                grid.append("#" * (n - 1) + ".")
                
        return grid