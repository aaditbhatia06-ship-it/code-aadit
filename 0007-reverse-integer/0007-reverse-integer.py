class Solution:
    def reverse(self, x: int) -> int:
        if(x>2**31-1 or x<(-2)**31):
            return 0
        y = 0
        z = abs(x)
        while(z!=0):
            rem = z %10
            y = y*10 + rem
            if y > 2147483647 :
                return 0
            z =  z//10
        if(x<0):
            return -y
        else:
            return y


         
            
             
        
        
            
