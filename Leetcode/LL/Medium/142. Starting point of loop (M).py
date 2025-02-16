class Solution:
    def detectCycle(self, head):
        # st = set()
        # while(temp):
        #     if(temp not in st):
        #         st.add(temp)
        #     else:
        #         return temp
        #     temp = temp.next
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
