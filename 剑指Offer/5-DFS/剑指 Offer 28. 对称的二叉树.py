# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def helper(left, right):
    if left == None and right == None:
        return True
    elif left == None or right == None:
        return False
    else:
        return left.val == right.val and helper(left.left, right.right) and helper(left.right, right.left)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return helper(root, root)
