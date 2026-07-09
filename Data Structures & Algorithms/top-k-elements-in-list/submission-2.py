class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for n in nums:
            hashmap[n] += 1
        sorted_hash = sorted(hashmap , key = lambda x: hashmap[x], reverse = True)
        return sorted_hash[:k]


         
        