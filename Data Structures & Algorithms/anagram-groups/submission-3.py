class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strs : 
            count = [0] * 26
            for l in word :
                count[ord(l) - ord("a")] += 1
            hashmap[tuple(count)].append(word)
            
        return list(hashmap.values())


        