class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = [[]for _ in range(len(nums)+1)]
        count = {}
        for num in nums : 
            count[num] = count.get(num, 0) + 1

        for key, value in count.items():
                freq[value].append(key)
        for c in range (len(freq)-1, -1, -1):
            for num in freq[c]:
                if len(res) == k :
                    break
                res.append(num)
        return res
                
                

        
        
        
                

            
        
        