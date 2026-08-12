class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}
        for c in s:
            smap[c] = 1 + smap.get(c, 0)
        
        for c in t:
            tmap[c] = 1 + tmap.get(c, 0)


        if smap == tmap:
            return True

        else:
            return False
