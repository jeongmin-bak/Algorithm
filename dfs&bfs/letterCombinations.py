# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            if len(digits) == len(path):
                result.append(path)
                return

            for digit in dic[digits[index]]:
                dfs(index+1, path+digit)

        if not digits:
            return []
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            "0": "+"
        }
        result = []
        dfs(0, "")
        return result
