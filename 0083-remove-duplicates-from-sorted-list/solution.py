# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        else:
            slow = head
            fast = head.next

            while fast:
                if fast.val != slow.val:
                    fast = fast.next
                    slow = slow.next
                else:
                    slow.next = fast.next
                    fast = fast.next
            return head
        
