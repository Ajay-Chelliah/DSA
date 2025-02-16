def reverseList(self, head):
    prev = None
    temp = head
    while temp:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front
    return prev
