class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for string in strs:
            h["".join(sorted(string))] = h.get("".join(sorted(string)), []) + [string]
        output = []
        for val in h.values():
            output.append(val)
        return output
        
        
        