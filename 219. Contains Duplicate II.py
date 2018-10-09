def containsNearbyDuplicate( nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    if len(nums) in [0, 1]:
        return False
    temp={}
    for k,v in enumerate(nums):
        if v not in temp:
            temp[v]=[k]
        else:
            temp[v]+=[k]
    for v in temp.values():
        if len(v)!=1:
            for x in set(v):

    return False
nums=[99,99]
k=2
print(containsNearbyDuplicate(nums,k))