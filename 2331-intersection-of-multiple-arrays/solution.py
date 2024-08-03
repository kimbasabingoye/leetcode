class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        d = defaultdict(int)

        for arr in nums:
            for i in range(len(arr)):
                d[arr[i]] += 1
                
        ans = []
        for key, value in d.items():
            if value == len(nums):
                ans.append(key)

        return sorted(ans)

