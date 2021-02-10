class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __iter__(self):
        p = self
        while p:
            yield p.val
            p = p.next


def addTwoNumbers(l1, l2):
    p1 = l1
    p2 = l2
    flag = False
    head = ListNode(-1)
    pr = head
    while p1 and p2:
        pr.next = ListNode((p1.val + p2.val + int(flag)) % 10)
        flag = p1.val + p2.val + int(flag) > 9
        pr = pr.next
        p1 = p1.next
        p2 = p2.next

    if p1:
        pr.next = p1
    elif p2:
        pr.next = p2

    while pr.next:
        value = (pr.next.val + int(flag)) % 10
        flag = (pr.next.val + int(flag)) > 9
        pr.next.val = value
        pr = pr.next

    if flag:
        pr.next = ListNode(1)
    return head.next


if __name__ == '__main__':
    n1 = ListNode(0)
    n2 = ListNode(0)
    assert addTwoNumbers(n1, n2).val == 0

    n1 = ListNode(5)
    n2 = ListNode(6)
    assert addTwoNumbers(n1, n2).val == 1
    assert addTwoNumbers(n1, n2).next.val == 1

    n1 = ListNode(9)
    n2 = ListNode(9)
    n2.next = ListNode(9)
    n2.next.next = ListNode(9)
    assert list(addTwoNumbers(n1, n2)) == [8, 0, 0, 1]
    assert list(addTwoNumbers(n2, n1)) == [8, 0, 0, 1]
