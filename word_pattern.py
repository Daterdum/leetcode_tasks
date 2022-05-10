class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_lst = s.split()

        if not len(pattern) == len(s_lst):
            return False

        pairs = {}
        for i in range(len(pattern)):
            cur_word = s_lst[i]
            if saved_word := pairs.get(pattern[i]):
                if saved_word != cur_word:
                    return False

            elif cur_word not in pairs.values():
                pairs[pattern[i]] = s_lst[i]

            else:
                return False

        print(pairs)

        return True
