# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        ls = []
        def dfs(root):
            if root !=None:
                dfs(root.left)
                ls.append(root.val)
                dfs(root.right)
        dfs(root)
        return ls[::-1][k-1]
