
class Solution(object):
    def longestZigZag(self, root):
        self.max_len = 0
        
        def dfs(node):
            if not node:
                return -1, -1
                
            left_l, left_r = dfs(node.left)
            right_l, right_r = dfs(node.right)
            
            l = 1 + left_r
            r = 1 + right_l
            
            self.max_len = max(self.max_len, l, r)
            return l, r
            
        dfs(root)
        return self.max_len