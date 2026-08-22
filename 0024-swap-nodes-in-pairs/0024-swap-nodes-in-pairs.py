# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        left = head
        prevleft = None
        res = None
        while(True):
            right = left 
            for i in range(1):
                right = right.next
            nextleft = right.next
            right.next = left
            left.next = nextleft
            if( prevleft is not None):
                prevleft.next = right
            else:
                res = right
            prevleft = left
            left = left.next
            if(left is None or left.next is None):
                break
        return res
        

        
            

