class MedianFinder:

    def __init__(self):
        self.maxHeap = [] #first half of the list of integers
        self.minHeap = [] #second half of the list of integers

    def addNum(self, num: int) -> None:
        if len(self.maxHeap) == len(self.minHeap):
            if not self.maxHeap:
                heapq.heappush(self.maxHeap, -num)
            elif num <= self.minHeap[0]:
                heapq.heappush(self.maxHeap, -num)
            else:
                cur = heapq.heappop(self.minHeap)
                heapq.heappush(self.maxHeap, -cur)
                heapq.heappush(self.minHeap, num)
        elif len(self.maxHeap) > len(self.minHeap):
            if -self.maxHeap[0] <= num:
                heapq.heappush(self.minHeap, num)
            else:
                cur = -(heapq.heappop(self.maxHeap))
                heapq.heappush(self.maxHeap, -num)
                heapq.heappush(self.minHeap, cur)
        

    def findMedian(self) -> float:
        if len(self.maxHeap) == len(self.minHeap):
            return (-(self.maxHeap[0]) + self.minHeap[0])/2
        else:
            return -(self.maxHeap[0])
