def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    k=0
    for x,y in zip(nums,range(len(nums))):
        if x==0:
            k+=1
            nums.pop(y)
    nums=nums+[0]*k
    return nums

nums=[0,1,0,2,3,4,5,0,5]
print(moveZeroes(nums))