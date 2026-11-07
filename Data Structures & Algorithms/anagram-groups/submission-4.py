class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            charcount = [0] * 26
            for char in s:
                charcount[ord(char) - ord('a')] += 1
            res[tuple(charcount)].append(s)
        
        return list(res.values())

        