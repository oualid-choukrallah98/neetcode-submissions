class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums :
            hashmap[num] = hashmap.get(num,0) + 1
        L = [[] for _ in range(len(nums)+1)]

        for index, value in hashmap.items():
            L[value].append(index)

        result = []
        for c in range(len(L)- 1, 0, -1):
            for num in L[c]:
                result.append(num)
                if len(result) == k :
                    return result
       
    



        