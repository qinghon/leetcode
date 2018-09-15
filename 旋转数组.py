def rotate( nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    if k>len(nums):
        k=k%len(nums)
    nums=nums[len(nums)-k:]+nums
    print(nums)
    nums=nums[:-k]
    return nums
li=[1,2,3,4,5,6,7]
print(rotate(li,8))