# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def _tree(nums):
    if nums:
        mid = int(len(nums)/2)
        p = TreeNode(val=nums[mid])
        p.left = _tree(nums[0:mid])
        p.right = _tree(nums[mid+1:])
        return p    

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return _tree(nums)
