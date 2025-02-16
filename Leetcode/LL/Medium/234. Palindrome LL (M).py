class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head) -> bool:
        temp = head
        s = ""
        while temp:
            s = s + str(temp.val)
            temp = temp.next
        if s == s[::-1]:
            return True
        return False
