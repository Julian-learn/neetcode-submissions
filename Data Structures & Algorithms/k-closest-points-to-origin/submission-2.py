class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def distance(point1, point2):
            return math.sqrt(((point1[0] - point2[0]))**2 + ((point1[1] - point2[1])**2))

        origin = [0, 0]
        distances = []
        result = []
        for p in points:
            distances.append([distance(p, origin), p])

        heapq.heapify(distances)
        while k > 0:
            result.append(heapq.heappop(distances)[1])
            k -= 1

        return result


        