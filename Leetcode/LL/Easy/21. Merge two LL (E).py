class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(self, list1, list2):
    temp1 = list1
    temp2 = list2
    if not temp1:
        return temp2
    if not temp2:
        return temp1
    if temp1.val <= temp2.val:
        head = ListNode(temp1.val)
        temp1 = temp1.next
    else:
        head = ListNode(temp2.val)
        temp2 = temp2.next
    temp = head
    while temp1 and temp2:
        if temp1.val <= temp2.val:
            temp.next = ListNode(temp1.val)
            temp1 = temp1.next
            temp = temp.next
        else:
            temp.next = ListNode(temp2.val)
            temp2 = temp2.next
            temp = temp.next
    while temp1:
        temp.next = ListNode(temp1.val)
        temp = temp.next
        temp1 = temp1.next
    while temp2:
        temp.next = ListNode(temp2.val)
        temp = temp.next
        temp2 = temp2.next
    return head
