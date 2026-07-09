class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)
    

    def decode(self, s: str) -> List[str]:
        decoded, i = [], 0
        
        while i < len(s) :
            j = i 
            while s[j] != "#":
                j = j + 1
            decoded.append(s[j+1:j+1+int(s[i:j])])
            i = j+1+int(s[i:j])
        return decoded
            

        

        
