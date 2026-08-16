"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        old_to_copy = { None : None}
        curr = head
        while curr:
            node = Node(curr.val)
            old_to_copy[curr] = node
            curr = curr.next


        curr = head 
        while curr : 
            node = old_to_copy[curr]
            node.next = old_to_copy[curr.next]
            node.random = old_to_copy[curr.random]
            curr = curr.next
        
        return old_to_copy[head]
        
        

        