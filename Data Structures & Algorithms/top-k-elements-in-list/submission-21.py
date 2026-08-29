class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = {}
        for num in nums :
            count[num] = count.get(num,0) + 1
        

        freq = [[] for _ in range(len(nums)+1)]

        for value, frequency in count.items(): 
            freq[frequency].append(value)
        
        for i in range(len(freq)-1, 0, -1): 
            for c in freq[i]:
                result.append(c)
                if len(result) == k:  
                    return result
        
        return result

        



    







    
        