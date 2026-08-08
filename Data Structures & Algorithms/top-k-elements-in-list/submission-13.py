class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = list()
        for num in nums : 
            count[num] = count.get(num,0) + 1
        sorted_c = dict(sorted(count.items(), key=lambda item: item[1], reverse = True))
        i = 0
        for key, value in sorted_c.items():
            result.append(key)
            i +=1
            if i  == k :
                break
        return result 







        