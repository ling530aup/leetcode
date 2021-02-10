# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inoder(root, record):
    if root:
        inoder(root.left, record)
        record.append(root.val)
        inoder(root.right, record)


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        record = []
        inoder(root, record)
        return record
