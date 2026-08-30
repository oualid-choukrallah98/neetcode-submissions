class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i, prev): 
            if (i, prev) in memo: 
                return memo[(i,prev)]

            if i == len(nums): 
                return 0 

            best = dfs(i+1, prev)
            if nums[i] > prev: 
                best = max(best, 1 + dfs(i+1,nums[i]))

            memo[(i,prev)] = best 
            
            return best 
        
        return dfs(0, float('-inf'))
            
        
    
            

    



        

                    