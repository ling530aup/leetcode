def inorder(root, ls):
    if root:
        inorder(root.left, ls)
        ls.append(root.val)
        inorder(root.right, ls)

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ls = []
        inorder(root, ls)
        return ls[k-1]
  
  
