# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        st = set()
        pa = headA
        pb = headB
        while pa:
            st.add(pa)
            pa = pa.next
        
        while pb:
            if pb in st:
                return pb
            pb = pb.next
        
        return None
