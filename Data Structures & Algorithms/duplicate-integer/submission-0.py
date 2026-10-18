class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        
        result = False

        seen = set()

        for n in nums:
            if n in seen:
                result = True
                break
            seen.add(n)

        return result