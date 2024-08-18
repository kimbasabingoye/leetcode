class Solution:
    def isValid(self, s: str) -> bool:
        close_match = {
            '{':'}',
            '[': ']',
            '(': ')'
        }
        stack = []
        for c in s:
            if c in close_match:
                stack.append(c)
            else:
                if not stack:
                    return False
                prev = stack.pop()
                if c != close_match[prev]:
                    return False
        return not stack


