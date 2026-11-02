class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}
        if len(s) != len(s):
            return False
        for i in s:
            map_s[i] = map_s.get(i, 0) + 1
        for j in t:
            map_t[j] = map_t.get(j, 0) + 1
        return map_s == map_t
        