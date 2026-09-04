class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        seen_numbers = {}
        for i in range(n):
            compliment = target - nums[i]
            if compliment in seen_numbers:
                return [seen_numbers[compliment], i]
            seen_numbers[nums[i]] = i
            
                
        
        