class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if(head is None or head.next is None):
            return head
        last = head
        n = 1
        while(last.next is not None):
            last = last.next 
            n+=1
        count = 1
        t = head
        k = k%n
        if(k==0):
            return head
        c = n-k
        while(t is not None):
            if(count == c):
                break
            else:
                t = t.next
                count+=1
        last.next = head
        head = t.next
        t.next = None
        return head


       
            
