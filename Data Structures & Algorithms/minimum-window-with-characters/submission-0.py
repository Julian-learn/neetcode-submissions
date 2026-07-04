class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""
        t_map = {}
        cur = {}
        
        for c in t:
            t_map[c] = t_map.get(c, 0) + 1
        
        matches = 0
        needed_matches = len(t_map)
        res = [-1, -1]
        res_len = float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            cur[c] = cur.get(c, 0) + 1

            if c in t_map and cur[c] == t_map[c]:
                matches += 1
            while matches == needed_matches:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                cur[s[l]] -= 1
                if s[l] in t_map and cur[s[l]] < t_map[s[l]]:
                    matches -= 1
                l += 1
        l, r = res[0], res[1]
        return s[l:r + 1] if res_len != float("infinity") else ""       
        
        
        