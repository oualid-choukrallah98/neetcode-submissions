class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        arr = [[]for _ in range(len(nums)+ 1)]
        res = []
        for num in nums: 
            freq[num] = freq.get(num,0)+ 1

        for value, cnt in freq.items():
            arr[cnt].append(value)

        for i in range(len(arr)-1, -1, -1):
            for c in arr[i]:
                res.append(c)
                if len(res) == k:
                    return res
    

