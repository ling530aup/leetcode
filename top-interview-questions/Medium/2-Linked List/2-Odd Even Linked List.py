# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEvenList(head):
    p = head
    head_odd = ListNode(-1)
    head_even = ListNode(-1)

    p_odd = head_odd
    p_even = head_even
    while p.next and p.next.next:
        p_odd.next = p
        p = p.next.next
        p_odd = p_odd.next

    p = head.next
    while p.next and p.next.next:
        p_even.next = p
        p = p.next.next
        p_even = p_even.next

    p_odd.next = head_even.next

    return head_odd.next


if __name__ == '__main__':
    pass
