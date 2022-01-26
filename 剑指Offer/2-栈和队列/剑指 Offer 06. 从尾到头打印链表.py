class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        p = head
        ls = []
        while p:
            ls.append(p.val)
            p = p.next
        return ls[::-1]
