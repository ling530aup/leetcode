# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


def zigzagLevelOrder(root: TreeNode) -> List[List[int]]:
    if not root:
        return []
    res = []
    queue = deque([root])
    # visited = set()

    index = 1
    while queue:
        level_node_n = len(queue)
        current_level = []

        for _ in range(level_node_n):
            top = queue.popleft()
            if top.left: queue.append(top.left)
            if top.right: queue.append(top.right)
            current_level.append(top.val)

        if index % 2:
            res.append(current_level)
        else:
            res.append(current_level[::-1])
        index += 1
    return res
