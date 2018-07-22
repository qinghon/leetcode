class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        l=0
        c=x^y
        for x in range(0,31):
            if c^(2**x)==(c-(2**x)):
                l+=1
        
        return l