class Solution:
    def rotateRight(self, head, k: int):
        temp = head
        c = 0
        if head == None:
            return None
        if head.next == None:
            return head
        while temp:
            c += 1
            temp = temp.next
        k = k % c
        if k == 0:
            return head

        # Step 3: Find the node at the (c - k) position
        temp = head
        for i in range(c - k - 1):
            temp = temp.next

        # Step 4: Rotate the list
        new_head = temp.next
        temp.next = None
        temp = new_head
        while temp.next:
            temp = temp.next
        temp.next = head

        return new_head
