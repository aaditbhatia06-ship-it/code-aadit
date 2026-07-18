class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        nodel = arr[0]
        onedel = 0
        ans = arr[0]
        p_no = nodel
            
        for i in range(1, len(arr)):
            p_no = nodel
            nodel = max(nodel + arr[i] , arr[i])
            onedel = max(onedel + arr[i], p_no)
            ans= max(ans,max(nodel,onedel))
        return ans
          
