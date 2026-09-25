class Solution(object):
    def solveSudoku(self, board):
        # Arrays of sets to keep track of used numbers
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []
        
        # 1. Initial pass: populate the sets and collect all empty cells
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty_cells.append((r, c))
                else:
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    # Calculate 1D box index (0-8) from 2D coordinates
                    box_idx = (r // 3) * 3 + (c // 3)
                    boxes[box_idx].add(val)
                    
        def backtrack(idx):
            # If we have filled all empty cells, the puzzle is solved
            if idx == len(empty_cells):
                return True
                
            r, c = empty_cells[idx]
            box_idx = (r // 3) * 3 + (c // 3)
            
            # Try placing digits 1-9
            for val in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                # O(1) check if the digit is valid
                if val not in rows[r] and val not in cols[c] and val not in boxes[box_idx]:
                    
                    # Place the digit and update our sets
                    board[r][c] = val
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_idx].add(val)
                    
                    # Move to the next empty cell in our pre-collected list
                    if backtrack(idx + 1):
                        return True
                        
                    # Backtrack: remove the digit and restore the sets
                    board[r][c] = '.'
                    rows[r].remove(val)
                    cols[c].remove(val)
                    boxes[box_idx].remove(val)
                    
            return False
            
        # Start the recursion from the 0th empty cell
        backtrack(0)