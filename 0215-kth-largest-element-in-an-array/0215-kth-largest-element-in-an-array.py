class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap,-nums[i])
        for i in range(k-1):
            heapq.heappop(heap)
        return -1*heapq.heappop(heap)
