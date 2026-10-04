# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        ans = ListNode(0, head)
        pre = ans

        while pre:
            while pre.next and pre.next.val == val:
                pre.next = pre.next.next
            pre = pre.next
        
        return ans.next