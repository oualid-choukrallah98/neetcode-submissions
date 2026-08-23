class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for i in range(len(points)):
            value = 0 
            for num in points[i]: 
                value += num ** 2
            distance.append([value,i])
        distance.sort()
        result = []
        for i in range(k): 
            _, idx = distance[i]
            result.append(points[idx])
        return result
