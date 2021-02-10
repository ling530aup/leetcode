# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


    
class Solution:
    def __init__(self):
        self.visited = []
        
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.check(root, root)
    
    def check(self, left, right):
        if left==None and right==None:
            return True
        if left==None or right==None:
            return False
        return left.val == right.val and self.check(left.left, right.right) and self.check(left.right,right.left)
    
