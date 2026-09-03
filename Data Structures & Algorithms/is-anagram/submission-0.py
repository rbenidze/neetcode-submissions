class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = list(t)
        b = list(s)
        a.sort()
        b.sort()
        return a == b
        
        