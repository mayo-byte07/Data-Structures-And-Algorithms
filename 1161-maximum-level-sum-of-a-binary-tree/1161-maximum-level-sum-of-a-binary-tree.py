class Solution(object):
    def maxLevelSum(self, root):
        if not root:
            return 0
            
        max_sum = float('-inf')
        max_level = 1
        current_level = 1
        
        queue = [root]
        
        while queue:
            level_sum = 0
            next_level = []
            for node in queue:
                level_sum += node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level
                
            queue = next_level
            current_level += 1
            
        return max_level