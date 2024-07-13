class Solution(object):
    def getEncryptedString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        r = []
        l = len(s)
        for i in range(l):
            r.append(s[(i+k)%l])
        return ''.join(r)
        
