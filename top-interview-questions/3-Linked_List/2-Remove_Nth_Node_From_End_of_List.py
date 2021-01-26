# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ls = []
        p = head
        while p:
            ls.append(p)
            p = p.next
            
        if len(ls) ==  n:
            return head.next
        p = ls[-n - 1]
        p.next = p.next.next
        return head
        
