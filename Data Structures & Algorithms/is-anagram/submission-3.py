class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        first_inp_list = list(s)
        second_inp_list = list(t)

        first_dict = {}
        second_dict = {}

        for char in first_inp_list:
            if char in first_dict:
                first_dict[char] += 1
            else:
                first_dict[char] = 1
        for char in second_inp_list:
            if char in second_dict:
                second_dict[char] += 1
            else:
                second_dict[char] = 1
    
        if first_dict == second_dict:
            return True
        else:
            return False