# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = []
        even = []

        if not head:
            return None
        e = 0
        while head:
            if not e:
                odd.append(head.val)
                e = 1
            else:
                even.append(head.val)
                e = 0
            head = head.next
        
        head = None
        tmp = head
        curent = head
        for i in odd:
            tmp = ListNode(i, None)

            if not head:
                head = tmp
                curent = tmp
            
            curent.next = tmp
            curent = curent.next
        
        for i in even:
            tmp = ListNode(i, None)

            curent.next = tmp
            curent = curent.next
        curent.next = None

        return head
            

