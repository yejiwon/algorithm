class Solution:
    def isValid(self, node, lower=float('-inf'), upper=float('inf')):
        if node is None:
            return True
        if lower < node.val < upper:
            return self.isValid(node.left, lower, node.val) and self.isValid(node.right, node.val, upper)
        return False
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root)