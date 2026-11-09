# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(curr):
            if not curr:
                return None
            
            if curr == p or curr == q:
                return curr
            
            l = dfs(curr.left)
            r = dfs(curr.right)
            if l and r:
                return curr
            if l:
                return l
            if r:
                return r
            
            return None
        
        return dfs(root)
        