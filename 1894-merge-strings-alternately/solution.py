class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        i1 = len(word1)
        i2 = len(word2)

        i = min(i1, i2)

        k = 0
        while k < i:
            res += word1[k]
            res += word2[k]
            k += 1

        if i == len(word1):
            res += word2[k:]
        else:
            res += word1[k:]

        return res
