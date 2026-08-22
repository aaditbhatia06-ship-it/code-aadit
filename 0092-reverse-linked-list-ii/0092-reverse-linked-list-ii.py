class Solution:
    def reverseBetween(self, head, left, right):
        if left == right:
            return head

        temp = head
        before = None
        pos = 1

        while temp is not None:
            if pos < left:
                before = temp
                temp = temp.next
                pos += 1
                continue

            curr = temp
            prev = None
            times = right - left + 1

            # reverse
            for _ in range(times):
                nex = curr.next
                curr.next = prev
                prev = curr
                curr = nex

            # connect
            if before is not None:
                before.next = prev
            else:
                head = prev

            temp.next = curr

            break

        return head