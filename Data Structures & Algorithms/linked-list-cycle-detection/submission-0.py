# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        isCycle = False
        s = head
        f = head

        while f and f.next:

            
            f = f.next.next
            s = s.next

            if f == s:
                isCycle = True
                break


        return isCycle