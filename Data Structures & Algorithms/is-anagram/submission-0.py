class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagrams need to contain the same number of characters
        if len(s) != len(t):
            return False
        # thank you python for the sorted function
        return sorted(s) == sorted(t)