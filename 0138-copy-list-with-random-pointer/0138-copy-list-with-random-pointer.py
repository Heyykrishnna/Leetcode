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
        d = {None: None}
        
        c = head
        while c:
            d[c] = Node(c.val)
            c = c.next
            
        c = head
        while c:
            d[c].next = d[c.next]
            d[c].random = d[c.random]
            c = c.next
            
        return d[head]