class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for arr in image:
            n = len(arr)
            left = 0
            right = n - 1
            while left <= right:
                if arr[left] == arr[right]:
                    arr[left] = arr[right] = arr[right] ^ 1
                left += 1
                right -= 1

        return image
