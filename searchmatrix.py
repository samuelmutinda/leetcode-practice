def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
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
    list2 =[]
    for i in range(0, len(matrix)):
        list2 += matrix[i]
    list2.sort()
    result = binary_search(list2, 0, len(list2)-1, target)
    if result == -1:
        return False
    return True
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(searchMatrix(matrix, 12222))