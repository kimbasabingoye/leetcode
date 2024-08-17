# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr = head
        sz = 0
        while curr:
            sz += 1
            curr = curr.next
        
        ans = 0
        curr = head
        i = sz-1
        while curr:
            ans += curr.val * 2**i
            i -= 1
            curr = curr.next
        
        return ans
        
