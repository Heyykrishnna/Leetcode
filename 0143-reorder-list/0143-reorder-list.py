# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next

        p, c = None, s.next
        s.next = None
        while c:
            nxt = c.next
            c.next = p
            p = c
            c = nxt

        a, b = head, p
        while b:
            t1, t2 = a.next, b.next
            a.next = b
            b.next = t1
            a, b = t1, t2