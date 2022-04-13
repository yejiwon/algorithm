class Solution:
    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        leftDepth = self.depth(root.left)
        rightDepth = self.depth(root.right)
        return abs(leftDepth - rightDepth) < 2 and self.isBalanced(root.left) and self.isBalanced(root.right)