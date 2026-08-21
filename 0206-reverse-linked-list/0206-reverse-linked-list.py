class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while(curr is not None):
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        return prev
        