# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        first = head
        second = head.next
        
        while second:
            print(first.val, second.val)
            if second.val != first.val:
                first.next = second
                first = second
            if not second.next and first.val == second.val:
                first.next = None
            second = second.next
        return head


