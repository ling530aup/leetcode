# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __iter__(self):
        p = self
        while p:
            yield p.val
            p = p.next

    def __repr__(self):
        return '->'.join(map(str, self))


def oddEvenList(head):
    p = head
    head_odd = ListNode(-1)
    head_even = ListNode(-1)

    p_odd = head_odd
    p_even = head_even

    while p and p.next:
        print('p = ', p.val)
        p_odd.next = p
        p_even.next = p.next

        p = p.next.next
        p_odd = p_odd.next
        p_even = p_even.next

    if p:
        p_odd.next = p
        p_even.next = None
        p_odd = p_odd.next
    ############
    p_odd.next = head_even.next

    return head_odd.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    print(oddEvenList(l1))
