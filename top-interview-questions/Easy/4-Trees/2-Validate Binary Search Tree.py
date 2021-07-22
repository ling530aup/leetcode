# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def is_bi_search_tree(root):
    def help(root, lower=float('-inf'), upper=float('inf')):
        if not root:
            return True
        if root.val < lower or root.val > upper:
            return False
        return help(root.left, lower, root.val) and help(root.right, root.val, upper)

    return help(root)
