class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}
        for char in s1:
            s1_map[char] = s1_map.get(char, 0) + 1

        s1_map_len = len(s1_map)
        for i in range(len(s2)):
            s2_map = {}
            matches = 0
            for j in range(i, len(s2)):
                s2_map[s2[j]] = s2_map.get(s2[j], 0) + 1
                if s1_map.get(s2[j], 0) < s2_map[s2[j]]:
                    break
                if s1_map.get(s2[j], 0) == s2_map[s2[j]]:
                    matches += 1
                if matches == s1_map_len:
                    return True
        return False