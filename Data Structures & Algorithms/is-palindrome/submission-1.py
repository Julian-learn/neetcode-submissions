class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", "")
        point1 = 0
        point2 = len(s) - 1
        while point1 < point2:
            if not s[point1].isalnum():
                point1 += 1
                continue
            if not s[point2].isalnum():
                point2 -= 1
                continue
            
            if not s[point1] == s[point2]:
                return False
            point1 +=1
            point2 -=1
        return True
                    

        