class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i],0)
        
        arr = []
        for num, count in count.items():
            arr.append([count,num])
        
        arr.sort()
        for i in range(len(arr)-1,-1,-1):
            if len(res) == k:
                return res

            res.append(arr[i][1])

        return res
