class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        for word in strs :
            l = [0] * 26
            for letter in word :
                l[ord(letter)- ord("a")] += 1

            count[tuple(l)].append(word)
        return list(count.values())
            
        

        

    

        