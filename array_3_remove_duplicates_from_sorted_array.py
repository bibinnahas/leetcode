def array_3_remove_duplicates(nums):
    if len(nums) <= 2:
        return len(nums)

    i = 1
    for j in range(2, len(nums)):
        if nums[j] != nums[1 - 1]:
            i += 1
            nums[i] = nums[j]
    return i + 1


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    nums1 = [1, 1, 1, 1, 2, 2, 3, 1, 3, 2]
    print(array_3_remove_duplicates(nums))
