class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        dumy = ListNode(-1)
        dum = dumy
        counter = 0
        sum = 0
        while (l1 or l2) or counter:
            sum = counter
            if l1:
                sum = sum + l1.val
                l1 = l1.next
            if l2:
                sum = sum + l2.val
                l2 = l2.next
            print(sum)
            if sum < 10:
                val = sum
                counter = 0
            else:
                val = sum % 10
                counter = 1
            dum.next = ListNode(val)
            dum = dum.next
        if counter == 1:
            dum.next = ListNode(1)
        return dumy.next
