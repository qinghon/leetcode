class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mydict={}
        for i,v in enumerate(nums):
            if target - v not in mydict:
                mydict[v]=i
            else:
                return [mydict[target-v],i]
