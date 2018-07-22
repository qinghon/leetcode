class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        num=0
        for x in J:
            num=num+S.count(x)
        return num