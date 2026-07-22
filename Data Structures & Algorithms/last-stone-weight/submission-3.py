class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            cur = abs(heapq.heappop(heap)) - abs(heapq.heappop(heap))
            heapq.heappush(heap, -cur)

        return abs(heap[0])
            

        
        