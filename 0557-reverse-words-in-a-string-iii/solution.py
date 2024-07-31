class Solution:
    def reverse(self, word):
        n = len(word)
        left = 0
        right = n-1
        while left < right:
            word[left], word[right] = word[right], word[left]
            left += 1
            right -= 1
        return word

    def reverseWords(self, s: str) -> str:
        ws = s.split(' ')
        words = [''.join(self.reverse(list(w))) for w in ws ]
        return ' '.join(words)
        
