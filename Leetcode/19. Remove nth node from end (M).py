class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n: int):
        temp = head
        c = 0
        while temp:
            c += 1
            temp = temp.next
        pos = c - n
        temp = head
        print(pos)
        if pos == 0:
            head = head.next
        c = 0
        while temp:
            c += 1
            if c == pos:
                temp.next = temp.next.next
            temp = temp.next
        return head
