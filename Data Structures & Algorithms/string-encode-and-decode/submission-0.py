from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            result += str(len(word)) + "#" + word

        return result


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find the #
            while s[j] != "#":
                j += 1

            # Everything before # is the length
            length = int(s[i:j])

            # Move to the start of the actual word
            j += 1

            # Read exactly 'length' characters
            word = s[j:j + length]

            result.append(word)

            # Move i to the next encoded string
            i = j + length

        return result