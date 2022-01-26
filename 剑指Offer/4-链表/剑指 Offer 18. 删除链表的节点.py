# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return head
        if head.val == val:
            return head.next
        prev, p = None, head
        while p:
            if p.val == val:
                prev.next = p.next
                return head
            prev = p
            p = p.next