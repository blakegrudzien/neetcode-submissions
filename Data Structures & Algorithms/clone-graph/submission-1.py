"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mapping = {}
        if not node:
            return node
        curr = Node(node.val)
        def dfs(old, curr):
            for neighbor in old.neighbors:
                if neighbor not in mapping:
                    mapping[neighbor] = Node(neighbor.val)
                    curr.neighbors.append(mapping[neighbor])
                    dfs(neighbor,mapping[neighbor])
                else:
                    curr.neighbors.append(mapping[neighbor])
        dfs(node, curr)

        return curr
                
            
            

        