class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded = encoded + f"{len(s)}#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        else:
            i = 0
            snum = ""
            decoded = []
            while s[i].isdigit():
                snum += s[i]
                i += 1
                if s[i] == "#":
                    decoded.append(s[i+1 : i+int(snum)+1])
                    i += int(snum) + 1
                    snum = ""
                    if i >= len(s):
                        break
            return decoded

             
