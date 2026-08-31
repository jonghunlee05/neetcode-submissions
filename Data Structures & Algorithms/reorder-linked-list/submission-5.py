# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        

        # get the midpoint
        s, f = head, head.next

        while f and f.next:
            s = s.next
            f = f.next.next


        # cut the second half
        first, second = head, s.next
        prev = s.next = None

        # reverse the second half
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # starting point of the second one starts with prev.
        second = prev

        # start inserting...
        while second: 
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        

