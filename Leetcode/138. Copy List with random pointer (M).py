class Solution:
    def copyRandomList(self, head):
        temp = head
        dict1 = {}
        c = 0
        if not head:
            return None
        while temp:
            dict1[temp] = Node(temp.val)
            temp = temp.next
        # for i,j in dict1.items():
        #     print(i,j)
        temp = head
        while temp:
            if temp.next:
                dict1[temp].next = dict1[temp.next]
            if temp.random:
                # print(temp.random)
                dict1[temp].random = dict1[temp.random]
            temp = temp.next
        return dict1[head]
