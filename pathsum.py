def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    def binary_search(arr, low, high, x):
        if high >= low:
            mid = (high + low) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return binary_search(arr, low, mid - 1, x)
            else:
                return binary_search(arr, mid + 1, high, x)
        else:
            return -1

    numstuple = tuple(nums)
    nums.sort()
    i = 0
    while i < len(nums):
        difference = target - nums[i]
        searchresult = binary_search(nums, 0, len(nums)-1, difference)
        if searchresult == -1:
            i += 1
        else:
            candidate1 = nums[i]
            candidate2 = nums[searchresult]
            break

    result = []
    j = 0
    while j < len(numstuple):
        if numstuple[j] == candidate1:
            result.append(j)
        elif numstuple[j] == candidate2:
            result.append(j)
        j += 1
    return result

nums = [3,3]
print(twoSum(nums, 6))