class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        full_list = list(range(len(nums) + 1))

        for num in full_list:
            if num not in nums:
                return num
                break