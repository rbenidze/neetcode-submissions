class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

        for char in s:
            if char.isalnum():
                cleaned += char

        cleaned = cleaned.lower()

        m = len(cleaned) // 2

        for i in range(m):
            if cleaned[i] != cleaned[len(cleaned) - 1 - i]:
                return False

        return True