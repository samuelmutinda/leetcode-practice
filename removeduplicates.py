def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    while i < len(nums):
        if i+1 < len(nums):
            if nums[i] == nums[i+1]:
                del nums[i+1]
            else:
                i += 1
        else:
            i+=1
    return len(nums)  
nums = [1,1]
print(removeDuplicates(nums))