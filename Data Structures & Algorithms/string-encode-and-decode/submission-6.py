class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for w in strs : 
            encoded += "".join(f"{len(w)}#{w}")
        return encoded 

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j = j+1
            l = int(s[i:j])
            result.append(s[j+1:j+1+l])
            i = l + j + 1
            
        return result         
