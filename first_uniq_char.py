class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = {}

        for letter in s:
            if letter in hash_map:
                hash_map[letter] += 1

            else:
                hash_map[letter] = 1

        for index, letter in enumerate(s):
            if hash_map[letter] == 1:
                return index

        return -1
