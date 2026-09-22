class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []
            
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return result