# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        stack = []
        
        temp = root
        visited = set()


        while k > 0:
            print("Looking at: ", temp.val)
            if not temp.left or temp.left in visited:
                print("lowest value: ", temp.val)
                k-=1
                if k == 0:
                    return temp.val
                visited.add(temp)
                if temp.right and temp.right not in visited and temp.right not in stack:
                    stack.append(temp.right)
                
                temp = stack.pop()
            else:
                if temp.right:
                    stack.append(temp.right)
                stack.append(temp)
                if temp.left not in visited:
                    temp = temp.left
                else:
                    temp = stack.pop()

            
        return temp.val
            
        
            
        
        