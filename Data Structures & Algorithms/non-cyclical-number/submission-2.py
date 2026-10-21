class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        while True:
            temp = list(str(n))
            list_num = list(int(x) for x in str(n))
            list_num_squared = [x**2 for x in list_num]
            sum_of_squares = sum(list_num_squared)

            if sum_of_squares == 1:
                return True

            if sum_of_squares in seen:
                return False
            elif sum_of_squares not in seen:
                seen.add(sum_of_squares)

            n = sum_of_squares

        