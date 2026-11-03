class Solution:
    def climbStairs(self, n: int) -> int:
        
        #idea is, there are two positions, one and two
        #the position to the left of one equals one plus two
        #we're going to be iterating down the stairs and considering-
        #for every possibility
        one, two = 1, 1


        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one