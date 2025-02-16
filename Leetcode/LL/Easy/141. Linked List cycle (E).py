class Solution:
    def hasCycle(self, head) -> bool:
        # st = set()
        # temp1 = head
        # while(temp1):
        #     temp1 = temp1.next
        #     if(temp1 in st):
        #         return True
        #     else:
        #         st.add(temp1)
        # return False
        if head == None:
            return False
        if head.next == None:
            return False
        tort = head
        hare = head
        while hare and hare.next:
            tort = tort.next
            hare = hare.next.next
            if tort == hare:
                return True
        return False
