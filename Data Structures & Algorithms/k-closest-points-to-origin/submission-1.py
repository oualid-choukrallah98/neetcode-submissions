class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for i in range(len(points)):
            value = 0 
            for num in points[i]: 
                value += num ** 2
            distance.append([value,i])
        heapq.heapify(distance)
        result = []
        i = 0
        while i < k : 
            _, idx = heapq.heappop(distance)
            result.append(points[idx])
            i += 1
        return result
