# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []
        
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        self._dfs(root, 0)
        return self.result
    
    def _dfs(self, root, level):
        if root:
            if len(self.result) < level + 1:
                self.result.append([])
                
            self.result[level].append(root.val)
            self._dfs(root.left, level+1)
            self._dfs(root.right, level+1)
   
