class Solution:
    def simplifyPath(self, path: str) -> str:
        path_elems = path.split('/')
        stack = []
        
        for c in path_elems:
            if c == '..':
                if stack:
                    stack.pop()
            elif c == '.' or not c:
                continue
            else:
                stack.append(c)
        
        return '/' + '/'.join(stack)
