class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = [[] for _ in range(len(nums)+1)]
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i],0)

        for value, count in count.items():
            frequency[count].append(value)

        res = []
        for c in range(len(frequency)-1,0,-1):
            if len(res) == k:
                break
            for j in range(len(frequency[c])):
                res.append(frequency[c][j])
        
        return res 


        