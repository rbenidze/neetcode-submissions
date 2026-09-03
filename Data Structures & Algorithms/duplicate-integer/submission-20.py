class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        seen = set()
        for i in range(n):
            seen.add(nums[i])
            if i+1 > len(seen):
                return True
        return False
    
    
