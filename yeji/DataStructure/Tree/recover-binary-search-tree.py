# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, node, visited, swap):
        if node:
            if node.left:
                visited, swap = self.inorder(node.left, visited, swap)
            
            if visited and visited[-1].val >= node.val:
                swap += [visited[-1], node]
            
            visited.append(node)
            
            if node.right:
                visited, swap = self.inorder(node.right, visited, swap)
        return visited, swap

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        visited, swap = self.inorder(root, visited=[], swap=[])
        swap[0].val, swap[-1].val = swap[-1].val, swap[0].val

""""
binary tree의 경우 root 기준 왼쪽 서브트리는 모두 root보다 작고 오른쪽 서브트리는 모두 root보다 크다
"""