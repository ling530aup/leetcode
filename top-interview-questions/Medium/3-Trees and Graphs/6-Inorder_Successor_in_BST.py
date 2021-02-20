def inorderSuccessor(root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
    res = None
    while root:
        if p.val < root.val:
            res = root
            root = root.left;
        else:
            root = root.right;
    return res
