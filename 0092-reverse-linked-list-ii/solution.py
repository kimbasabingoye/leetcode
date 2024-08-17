# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        i = 0
        curr = dummy
        # find the node before the left th node
        while i < left-1:
            curr = curr.next
            i += 1
        group_prev = curr
        first_node = curr.next
        #print(group_prev.val)
        
        prev = None
        curr = curr.next
        i = right - left + 1
        while i:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            i -= 1
        group_prev.next = prev
        first_node.next = curr
            
        return dummy.next
