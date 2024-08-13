# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # find the midle
        # find the node before the middle node
        # make the node before the middle point to the node after the middle
        if not head.next:
            head = None
            return head

        fast = head.next.next
        prev_mid = head
        while fast and fast.next:
            prev_mid = prev_mid.next
            fast = fast.next.next
        
        # make prev next be mid next
        prev_mid.next = prev_mid.next.next
        
        return head


        
