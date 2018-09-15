def thirdMax(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums=list(set(nums))
    nums.sort(reverse=True)
    if len(nums)<3:
        return nums[0]
    else:
        return nums[2]

nums=[1,1,2,5,6,9,5,1,7,5,65,]

print(thirdMax(nums))