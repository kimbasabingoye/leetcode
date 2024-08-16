# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        group_num = 1
        sz = 0
        n_processed = 0
        
        # calculate the size of the linked list
        curr = head
        while curr:
            sz += 1
            curr = curr.next
        
        prev = None
        curr = head

        while curr:
            length = min(group_num, sz - n_processed)
            
            if length % 2 == 0:
                # Reverse this even-length group
                group_prev = prev
                #print(f"Group {group_num} to be reversed")
                #print(f"GROUP PREV: {group_prev.val}")
                prev2 = None
                first_node = curr # save the first node of the group to reconnect later

                for i in range(length):
                    next_node = curr.next
                    curr.next = prev2
                    prev2 = curr
                    curr = next_node
                
                # connect the reversed part back to the main list
                if group_prev:
                    group_prev.next = prev2
                else:
                    head = prev2 # If the first group is reversed, update the head
                
                first_node.next = curr
                prev = first_node
            else:
                # Move the pointer normally for odd-length groups
                for i in range(length):
                    prev = curr
                    curr = curr.next
            
            group_num += 1
            n_processed += length 
            
        return head


        
