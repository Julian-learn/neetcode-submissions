class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        countmap = {}

        for t in tasks:
            countmap[t] = 1 + countmap.get(t, 0)

        heap = []
        for task, count in countmap.items():
            heap.append([-count, task])

        heapq.heapify(heap)
        q = deque()
        res = 0
        while heap or q:
            if heap:
                cur = heapq.heappop(heap)
                cur[0] += 1
                if cur[0] == 0:
                    cur = None
            else:
                cur = None
            
            q.appendleft(cur)
            res += 1

            if len(q) > n:
                right = q.pop()
                if right:
                    heapq.heappush(heap, right)

            if not heap and all(x is None for x in q):
                break

        return res