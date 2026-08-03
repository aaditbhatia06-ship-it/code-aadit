class Solution:
    def intervalIntersection(self, firstint: List[List[int]], secondint: List[List[int]]) -> List[List[int]]:
        n = len(firstint)
        m = len(secondint)
        i = 0
        j = 0
        inte=[]
        while (i<n and j < m):  
            start1 = firstint[i][0] 
            end1 = firstint[i][1]
            start2 = secondint[j][0]
            end2 = secondint[j][1]
            end3 = end1
            end4 =end2
            if(start1<=start2):
                if(end1>=start2):
                    start1 = max(start1,start2) 
                    end1 = min(end1,end2)
                    inte.append([start1,end1])
            else:
                if(end2>=start1):
                    start2 =max(start1,start2)
                    end2 = min(end1,end2)
                    inte.append([start2,end2])
            if(end3<=end4):
                i +=1
            else:
                j+=1
        return inte

       