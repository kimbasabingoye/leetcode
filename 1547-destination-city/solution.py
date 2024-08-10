class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        have_dest = set()

        for e in paths:
            have_dest.add(e[0])
        
        for e in paths:
            if e[1] not in have_dest:
                return e[1]
            
        
