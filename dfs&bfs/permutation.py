# https://leetcode.com/problems/permutations/description/

import itertools

def permutations(input_data):
    def dfs(lst):
        if lst is None:
            lst = []
        if len(lst) == len(input_data):
            result.append(lst)
            return

        for s in input_data:
            if s not in lst:
                dfs(lst+[s])

    result = []
    dfs([])
    return result

def permute(nums):
    return list(itertools.permutations(nums))

input_data = [1,2,3,4]
print(permutations(input_data))
print(permute([1,2,3]))
