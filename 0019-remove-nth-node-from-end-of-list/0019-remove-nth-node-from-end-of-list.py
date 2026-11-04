# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        d = ListNode(0, head)
        l = d
        r = head
        for _ in range(n):
            r = r.next
        while r:
            l = l.next
            r = r.next
        l.next = l.next.next
        return d.next