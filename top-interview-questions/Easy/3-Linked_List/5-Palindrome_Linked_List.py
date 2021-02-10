# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ls = []
        p = head
        while p:
            ls.append(p.val)
            p = p.next
        return ls == ls[::-1]
 
