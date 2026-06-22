"""def firstPalindrome(words):
    for word in words:
        if word == word[::-1]:
            return word
    return ""

# Example
print(firstPalindrome(["abc","car","ada","racecar","cool"]))
print(firstPalindrome(["notapalindrome","racecar"]))"""
#----------------------------------------------------
"""def findIntersectionValues(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    answer1 = sum(1 for x in nums1 if x in set2)
    answer2 = sum(1 for x in nums2 if x in set1)

    return [answer1, answer2]

# Example
print(findIntersectionValues([2,3,2], [1,2]))
print(findIntersectionValues([4,3,2,3,1], [2,2,5,2,3,6]))"""
#-------------------------------------------------------------------
"""def sumCounts(nums):
    n = len(nums)
    total = 0

    for i in range(n):
        distinct = set()
        for j in range(i, n):
            distinct.add(nums[j])
            total += len(distinct) ** 2

    return total

# Example
print(sumCounts([1,2,1]))
print(sumCounts([1,1]))"""
#---------------------------------------------------------------------------
"""def countPairs(nums, k):
    n = len(nums)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j] and (i * j) % k == 0:
                count += 1

    return count

# Example
print(countPairs([3,1,2,2,2,1,3], 2))
print(countPairs([1,2,3,4], 1))"""
#--------------------------------------------------------------------------------
"""def findMaximum(arr):
    if not arr:
        return None

    maximum = arr[0]

    for num in arr:
        if num > maximum:
            maximum = num

    return maximum

# Test Cases
print(findMaximum([1,2,3,4,5]))
print(findMaximum([7,7,7,7,7]))
print(findMaximum([-10,2,3,-4,5]))"""
#-----------------------------------------------------------------------------
"""def sortAndFindMax(arr):
    if not arr:
        return "List is empty"

    arr.sort()      # Efficient sorting (Timsort)
    return arr[-1]

# Test Cases
print(sortAndFindMax([]))
print(sortAndFindMax([5]))
print(sortAndFindMax([3,3,3,3,3]))"""
#-----------------------------------------------------------------------------
"""def uniqueElements(arr):
    seen = set()
    result = []

    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result

# Test Cases
print(uniqueElements([3,7,3,5,2,5,9,2]))
print(uniqueElements([-1,2,-1,3,2,-2]))
print(uniqueElements([1000000,999999,1000000]))"""
#---------------------------------------------------------------------------------
"""def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr

# Example
print(bubbleSort([64,34,25,12,22,11,90]))"""
#-----------------------------------------------------------------------------
"""def binarySearch(arr, key):
    arr.sort()  # Binary search requires sorted array

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return f"Element {key} is found at position {mid+1}"

        elif arr[mid] < key:
            low = mid + 1

        else:
            high = mid - 1

    return f"Element {key} is not found"

# Test Cases
print(binarySearch([3,4,6,-9,10,8,9,30], 10))
print(binarySearch([3,4,6,-9,10,8,9,30], 100))"""
#--------------------------------------------------------------------------------
"""def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Example
nums = [5,2,3,1]
print(mergeSort(nums))"""
#------------------------------------------------------------------------------
