class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        low = matrix[0][0]
        high = matrix[n-1][m-1]
        res = 0
        while(low<=high):
            guess = (low+high)//2
            row = 0
            col = m-1
            count = 0
            while(col>=0 and row<n):
                if(matrix[row][col]<=guess):
                    count = count + col+1
                    row+=1
                else:
                    col-=1
            if(count<k):
                low = guess+1
            else:
                res = guess
                high = guess-1
        return res



