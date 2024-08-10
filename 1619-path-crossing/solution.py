class Solution:
    def isPathCrossing(self, path: str) -> bool:
        curr_cor = (0, 0)
        d = defaultdict(int)
        d[(0, 0)] = 1
        for s in path:
            if s == 'N':
                l = list(curr_cor)
                l[1] += 1
                curr_cor = tuple(l)
            elif s == 'S':
                l = list(curr_cor)
                l[1] -= 1
                curr_cor = tuple(l)
            elif s == 'E':
                l = list(curr_cor)
                l[0] += 1
                curr_cor = tuple(l)
            elif s == 'W':
                l = list(curr_cor)
                l[0] -= 1
                curr_cor = tuple(l)
            
            d[curr_cor] += 1
        print(d)
        for v in d.values():
            if v >= 2:
                return True
        return False
