
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        left = head
        prevleft = None
        res = None
        while(True):
            right = left 
            for i in range(k-1):
                if (right is None):
                    return res
                right = right.next
            if (right is None):
                break
            nextleft = right.next
            curr = left
            prev = nextleft
            for i in range(k):
                nex = curr.next
                curr.next = prev
                prev = curr
                curr = nex
            if( prevleft is not None):
                prevleft.next = right
            else:
                res = right
            prevleft = left
            left = curr
            if(left is None or left.next is None):
                break
        return res