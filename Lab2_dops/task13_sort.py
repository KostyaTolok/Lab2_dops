import random


def quick_sort(nums, first, last):
    if first >= last:
        return

    i, j = first, last
    p = nums[random.randint(first, last)]
    while i <= j:

        while nums[i] < p:
            i += 1

        while nums[j] > p:
            j -= 1

        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    quick_sort(nums, first, j)
    quick_sort(nums, i, last)


def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left_half = nums[:mid]
        right_half = nums[mid:]
        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                nums[k] = left_half[i]
                i += 1
            else:
                nums[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            nums[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            nums[k] = right_half[j]
            j += 1
            k += 1


def radix_sort(nums):
    length = len(str(max(nums)))
    rang = 10
    for i in range(length):
        radix_sorted = [[] for _ in range(rang)]
        for num in nums:
            index = (num // (10 ** i)) % 10
            radix_sorted[index].append(num)
        nums = []
        for k in range(rang):
            if len(radix_sorted[k]) != 0:
                nums.extend(radix_sorted[k])

    return nums


def main():
    values = [32, 42, 1, 1, 332, 12]
    # quick_sort(values, 0, len(values) - 1)
    # merge_sort(values)
    values = radix_sort(values)
    print(values)


if __name__ == '__main__':
    main()
