class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = {}
        def dfs(i): 
            if i in memo : 
                return memo[i]

            if i == len(s): 
                return True 
            
            for word in wordDict: 
                if s[i: i+len(word)] == word and i + len(word) <= len(s): 
                    if dfs(i+ len(word)): 
                        return True 

            memo[i] = False
            return False 
        
        return dfs(0)
            
        