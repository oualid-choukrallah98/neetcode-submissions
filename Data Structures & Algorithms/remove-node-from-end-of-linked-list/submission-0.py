# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        lenght = 0
        i = 0
        while slow:
            slow = slow.next
            lenght += 1 
        dummy = ListNode(0,head)
        prev = dummy
        while i < lenght-n:
            prev = prev.next
            i += 1

        prev.next = prev.next.next
        return dummy.next

        



        

        
        