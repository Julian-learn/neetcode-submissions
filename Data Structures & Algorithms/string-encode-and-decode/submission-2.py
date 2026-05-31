class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

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

             
