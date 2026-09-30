class Solution(object):
    def searchBST(self, root, val):
        current = root
        
        while current:
            if current.val == val:
                return current
            elif val < current.val:
                current = current.left
            else:
                current = current.right
        return None