class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        result = False
        cleaned = ""

        for char in s:
            if char.isalnum():
                cleaned += char
        
        lowercase_cleaned = cleaned.lower()

        if lowercase_cleaned == lowercase_cleaned[::-1]:
            result = True

        return result
        