class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hashmap = defaultdict(list)
        for word in strs: 
            freq = [0] * 26
            for l in word: 
                freq[ord(l)-ord("a")] += 1
            
            hashmap[tuple(freq)].append(word)
        
        
        for value in hashmap.values(): 
            result.append(value)
        
        return result