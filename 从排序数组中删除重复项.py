

def removeDuplicates( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
        if len(nums)==0:
            return 0
        l=1
        for x in range(1,len(nums)):
            if nums[x-1]==nums[x]:
                continue
            else:
                nums[l]=nums[x]
                l+=1
                
        return l

nums=[0,0,1,1,1,2,2,3,3,4,4,4]
print(removeDuplicates(nums))