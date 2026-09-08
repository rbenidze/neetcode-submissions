class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_list = []

        for text in strs:
            encoded_list.append(f"{len(text)}#{text}")

        return "".join(encoded_list)

    def decode(self, s: str) -> List[str]:
        decode_list = []
        i = 0
        n = len(s)

        while i < n:
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            start = j + 1
            end = start + length

            word = s[start:end]
            decode_list.append(word)

            i = end

        return decode_list


