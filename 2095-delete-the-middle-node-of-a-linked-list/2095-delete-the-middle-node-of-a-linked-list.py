class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        prev = None
        if head is None or head.next is None:
            return None
        while(fast is not None and fast.next is not None):
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next=slow.next
        return head
      
    
     

        