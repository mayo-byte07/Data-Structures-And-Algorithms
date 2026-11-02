class Solution(object):
    def leafSimilar(self, root1, root2):
        def collect_leaves(node, leaves):
            if not node:
                return
            if not node.left and not node.right:
                leaves.append(node.val)
                return
            collect_leaves(node.left, leaves)
            collect_leaves(node.right, leaves)
            
        leaves1 = []
        leaves2 = []
        
        collect_leaves(root1, leaves1)
        collect_leaves(root2, leaves2)
        
        return leaves1 == leaves2