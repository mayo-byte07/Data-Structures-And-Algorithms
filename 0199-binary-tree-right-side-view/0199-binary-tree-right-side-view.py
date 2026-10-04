class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
            
        result = []
        queue = [root]
        
        while queue:
            result.append(queue[-1].val)
            next_level = []
            for node in queue:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                    
            queue = next_level
            
        return result