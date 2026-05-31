class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted_list = sorted(s)
        t_sorted_list = sorted(t)
        return s_sorted_list == t_sorted_list