# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        pre, p = None, head
        
        while p:
            tmp = p.next
            p.next = pre
            pre = p
            p = tmp
        return pre
        
