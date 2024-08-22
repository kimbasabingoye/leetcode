class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)
        ans = [-1] * n1
        elems = {}
        stack = []

        for i in range(n2):
            curr = nums2[i]

            while stack and curr > stack[-1]:
                e = stack.pop()
                elems[e] = curr
            stack.append(curr)
        
        while stack:
            e = stack.pop()
            elems[e] = -1

        for j in range(n1):
            ans[j] = elems[nums1[j]]


        return ans
