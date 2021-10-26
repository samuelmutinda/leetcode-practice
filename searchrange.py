def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    def binary_search (arr, start, end, x):
        if end >= start:
            mid = start + (end- start)//2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return binary_search(arr, start, mid-1, x)
            else:
                return binary_search(arr, mid+1, end, x)
        else:
            return -1

    if nums != []:
        index = binary_search(nums, 0, len(nums)-1, target)
        if index == -1:
            return [-1, -1]
        i = index
        while i+1 < len(nums) and nums[i+1] == target:
            i += 1
        j = index
        while j-1 >= 0 and nums[j-1] == target:
            j -= 1
        result = []
        result.append(j)
        result.append(i)
        return result
    return [-1, -1]
nums = [1,1,2]
print(searchRange(nums, 1))