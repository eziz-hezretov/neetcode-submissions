class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        seen = {}

        for num in nums:
            if num not in seen:
                seen[num] = 0
            if num in seen:
                seen[num] += 1

        for key, occurrences in seen.items():
            if occurrences == 1:
                return key
            