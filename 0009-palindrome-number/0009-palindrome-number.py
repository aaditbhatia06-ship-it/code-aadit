class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        op = 0
        y =x
        while x>0:
            rem = x % 10
            x = x//10
            op = op * 10 + rem
        if op==y:
            return True
        else:
            return False

    