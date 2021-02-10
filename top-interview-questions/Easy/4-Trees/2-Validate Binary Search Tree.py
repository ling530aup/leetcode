# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def in_order(root,visit):
    if root:
        in_order(root.left,visit)
        visit.append(root.val)
        # print("visited -> ", root.val)
        in_order(root.right,visit)
    
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        visit = [] 
        in_order(root,visit)
        for i in range(len(visit)-1):
            if visit[i] >= visit[i+1]:
                return False
        return True
