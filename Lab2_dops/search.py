def bin_search(nums, value):

    mid = len(nums) // 2
    first, last = 0, len(nums) - 1

    while first <= last:
        if nums[mid] == value:
            return mid
        if value > nums[mid]:
            first = mid + 1
        else:
            last = mid - 1
        mid = (last + first) // 2

    return ValueError()


a = [12, 44, 3, 12, 1]
a.sort()
print(a)
print(bin_search(a, 44))