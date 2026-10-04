class Solution(object):
    def maxPathSum(self, root):
        self.max_sum = float('-inf')
        def dfs(node):
            if not node:
                return 0
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)
            current_arch_sum = node.val + left_max + right_max
            if current_arch_sum > self.max_sum:
                self.max_sum = current_arch_sum
            return node.val + max(left_max, right_max)
            
        dfs(root)
        return self.max_sum