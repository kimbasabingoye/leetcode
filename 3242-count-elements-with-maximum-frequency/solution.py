class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        maxFreq = 0

        for e in nums:
            cnt[e] += 1

            maxFreq = max(maxFreq, cnt[e])


        #target  = max(cnt.values())

        ans = 0

        for k, v in cnt.items():
            if v == maxFreq:
                ans += v
        
        return ans
