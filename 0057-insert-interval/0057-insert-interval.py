class Solution:
    def insert(self, intervals: List[List[int]], newinterval: List[int]) -> List[List[int]]:
        intervals.sort()
        merged = []
        ans = []
        if len(intervals)==0:
            return [newinterval]

        insert = False
        for i in range(len(intervals)):
            if (insert == False and intervals[i][0]>= newinterval[0]):
                merged.append(newinterval)
                insert = True
            merged.append(intervals[i])

        if not insert:
            merged.append(newinterval)

        start1 = merged[0][0]
        end1 = merged[0][1]
        for i in range(1,len(merged)):
            start2 = merged[i][0]
            end2 = merged[i][1]
            if(end1>=start2):
                start1 = start1
                end1 =max(end1,end2)
            else:
                ans.append([start1,end1])
                start1 =start2
                end1 = end2
        ans.append([start1,end1])
        return ans


        


       