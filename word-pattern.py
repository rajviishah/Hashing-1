# TC: O(n)
# SC: O(26 + m); m = number of unique words in s (map_word), 26 for map_char
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_word = {}
        map_char = {}

        words = s.split(' ')
        if len(words) != len(pattern):
            return False

        for c, w in zip(pattern, words):
            if c not in map_char:
                if w in map_word:
                    return False
                else:
                    map_char[c] = w
                    map_word[w] = c
            else:
                if map_char[c] != w:
                    return False
        return True