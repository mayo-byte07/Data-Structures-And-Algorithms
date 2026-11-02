
class Solution(object):
    def goodNodes(self, root):
        def dfs(node, max_val):
            if not node:
                return 0
            
            count = 1 if node.val >= max_val else 0
            new_max = max(max_val, node.val)
            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)
            
            return count
            
        return dfs(root, root.val)