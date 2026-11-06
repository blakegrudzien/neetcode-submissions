# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = [root]
        if not root:
            return []

        while q:
            cur = []
            for i in range(len(q)):   
                n = q.pop(0)
                if n:
                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
                    cur.append(n.val)
            res.append(cur)
        return res
                
        