class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        index = len(digits) - 1

        while index >= 0:
            if 0 <= digits[index] < 9:
                digits[index] += 1
                return digits
            elif index == 0 and digits[index] == 9:
                digits[index] = 0            
                digits.insert(0, 1)
                return digits
            else:
                digits[index] = 0
                index -= 1
            

            


