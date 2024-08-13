# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        #print(mid.val)
        
        # find the last node of first half
        curr = head
        while curr.next != slow:
            curr = curr.next
        curr.next = None
        #print(curr.val)

        # Reverse second half
        prev = None 
        curr = mid
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        curr1 = prev
        curr2 = head
        ans = 0
        while curr1 and curr2:
            ans = max(ans, curr1.val + curr2.val)
            curr1 = curr1.next
            curr2 = curr2.next
        
        return ans
