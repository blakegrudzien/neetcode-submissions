# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        q = []
        q.append(root)
        
        while q:
            curr = q.pop(0)
            print(curr.val)
            t = curr.right
            curr.right = curr.left 
            curr.left = t
            if curr.left:
                q.append(curr.left)
            if curr.right: 
                q.append(curr.right)
        return root

        