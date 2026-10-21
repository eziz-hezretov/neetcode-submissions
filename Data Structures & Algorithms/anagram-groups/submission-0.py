class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dictionary = {}

        sorted_list = []

        for item in strs:
            item = ''.join(sorted(item))
            sorted_list.append(item)
        
        for index, value in enumerate(sorted_list):
            if value not in dictionary:
               dictionary[value] = [index]
            else:
                dictionary[value].append(index)
        
        new_list = []

        for key, value in dictionary.items():
            group = []

            for val in value:
                group.append(strs[val])
            new_list.append(group)

        return new_list


