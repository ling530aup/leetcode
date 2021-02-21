"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        queue = deque([root])
        #visited = set()
        while queue:
            current_level_n = len(queue)
            for i in range(current_level_n):
                top = queue.popleft()
                if top.left: queue.append(top.left)
                if top.right: queue.append(top.right)
                if i != current_level_n-1:
                    top.next = queue[0]
        return root
                
        
        
