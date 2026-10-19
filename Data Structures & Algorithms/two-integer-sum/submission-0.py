class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for index, value in enumerate(nums):
            interest = target - value
            if not interest in seen:
                seen[value] = index
            else:
                return [seen[interest], index]
