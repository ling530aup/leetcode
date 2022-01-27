# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if root == None:
                return root
            else:
                root.left, root.right = root.right, root.left
                root.left = dfs(root.left)
                root.right = dfs(root.right)
                return root

        return dfs(root)
