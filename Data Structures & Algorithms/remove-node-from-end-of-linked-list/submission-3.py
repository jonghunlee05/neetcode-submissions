# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        # another approach is reverse the list first. 
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # make a copy of it. 
        dummy = ListNode(0, prev)
        before_remove = dummy

        # move it before the target:
        for i in range(n - 1):
            before_remove = before_remove.next
        

        # now cut it!
        before_remove.next = before_remove.next.next


        # now bring back the reverse list again. 
        prev, curr = None, dummy.next

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp


        return prev

