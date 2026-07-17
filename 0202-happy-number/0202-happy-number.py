class Solution:
    def isHappy(self, n: int) -> bool:
        def square(n):
            su = 0
            while (n>0):
                d = n%10
                n //=10
                su = su + (d*d)
            return su
        slow = n
        fast = n
        while(fast!=1):
            slow= square(slow)
            fast = square(fast)
            fast = square(fast)
            if(slow==fast and slow!=1):
                return False
        return True