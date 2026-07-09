class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = [[] for _ in range(len(nums)+1)]
        counts = {}
        result = []
        for i in range(len(nums)):
            counts[nums[i]] = counts.get(nums[i],0) + 1
        for value, count in counts.items():
            frequency[count].append(value)
        
        for c in range(len(frequency)-1,0,-1):
            for num in frequency[c]:
                result.append(num)
            if len(result) == k:
                return result 

        