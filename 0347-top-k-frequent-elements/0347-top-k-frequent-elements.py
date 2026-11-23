class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        rep = Counter(nums)
        min_heap = []

        for num, count in rep.items():
            heapq.heappush(min_heap, (count, num))
            
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [num for count, num in min_heap]
