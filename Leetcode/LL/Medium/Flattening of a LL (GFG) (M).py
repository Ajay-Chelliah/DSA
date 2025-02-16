class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None


class Solution:
    def flatten(self, root):
        temp = root
        list1 = []
        head = Node(-1)
        while temp:
            p1 = temp
            while p1:
                list1.append(p1.data)
                p1 = p1.bottom
            temp = temp.next
        temp1 = head
        list2 = sorted(list1)
        for i in list2:
            print(i, end=" ")
            # temp1.next = Node(i)
            # temp1 = temp1.next
