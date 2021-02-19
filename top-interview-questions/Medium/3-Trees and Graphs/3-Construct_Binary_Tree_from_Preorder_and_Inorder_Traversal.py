# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def _help(preorder, inorder):
    if len(preorder) == len(inorder) == 0:
        return

    root = TreeNode(preorder[0])
    # preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    for inorder_i, item in enumerate(inorder):
        if item == root.val:
            break
    left_preoder = preorder[1:inorder_i + 1]
    left_inorder = inorder[:inorder_i]

    right_preoder = preorder[inorder_i + 1:]
    right_inorder = inorder[inorder_i + 1:]

    root.left = _help(left_preoder, left_inorder)
    root.right = _help(right_preoder, right_inorder)
    return root


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return _help(preorder, inorder)
