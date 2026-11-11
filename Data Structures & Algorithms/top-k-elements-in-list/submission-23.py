class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        hashmap = {}
        listnum = [[] for _ in range(len(nums)+1)]
        for num in nums: 
            hashmap[num] = hashmap.get(num, 0) + 1
        
        for key, value in hashmap.items(): 
            listnum[value].append(key)
        
        for c in range(len(listnum)-1, -1, -1): 
            for element in listnum[c]: 
                result.append(element)
                if k == len(result):
                    return result


        
    






    

        