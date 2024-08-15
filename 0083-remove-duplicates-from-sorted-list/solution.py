# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        first = head
        second = head.next
        while second:
            if first.val != second.val:
                first.next = second
                first = second
            second = second.next
        first.next = None
        return head
        
