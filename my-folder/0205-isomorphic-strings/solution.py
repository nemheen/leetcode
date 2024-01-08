
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_s_to_t = {}
        char_t_to_s = {}

        for i in range(len(s)):
            if s[i] not in char_s_to_t and t[i] not in char_t_to_s:
                char_s_to_t[s[i]] = t[i]
                char_t_to_s[t[i]] = s[i]
            elif char_s_to_t.get(s[i]) != t[i] or char_t_to_s.get(t[i]) != s[i]:
                return False

        return True

