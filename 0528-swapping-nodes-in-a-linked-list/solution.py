# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
       length = 0
       curr = head
       frontNode = endNode = None

       while curr:
        length += 1
        if endNode is not None:
            endNode = endNode.next
        if length == k:
            frontNode = curr
            endNode = head
        
        curr = curr.next

       frontNode.val, endNode.val = endNode.val, frontNode.val

       return head
