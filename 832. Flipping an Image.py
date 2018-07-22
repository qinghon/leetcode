class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B=[]
        for A_1 in A:
            A_1.reverse()
            for v in range(len(A_1)):
                if A_1[v]==0:
                    A_1[v]=1
                else:
                    A_1[v]=0
            B.append(A_1)
        return B