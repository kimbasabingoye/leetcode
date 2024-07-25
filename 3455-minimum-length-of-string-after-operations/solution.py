class Solution:
    def cnt_freq(self, input_string):
        freq_dict = {}
        for char in input_string:
            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1
        return freq_dict

    def minimumLength(self, s: str) -> int:
        res = 0
        freq = self.cnt_freq(s)
        for _, value in freq.items():
            if value % 2:
                res += 1
            else:
                res += 2
        return res
        
