class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = numbers
        i = 0
        j = len(numbers) - 1
        while i < j:
            if s[i] + s[j] < target:
                i += 1
            elif s[i] + s[j] > target:
                j -= 1
            else:
                return [i+1,j+1] 
        