class Note:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self, head):
        self.head = Note(0)
        self.tail = self.head
        self.size = 0

    def append(self, x):
        self.tail.next = Note(x)
        self.tail = self.tail.next
        self.size = self.size + 1

    def find_index(self, x):
        p = self.head.next
        count = 1
        while p!= None:
            if p.data != x:
                p = p.next
                count = count + 1
            else:
                return count
        return -1
