def array_3_remove_duplicates(nums):
    if len(nums) <= 2:
        return len(nums)

    i = 2
    for j in range(2, len(nums)):
        if nums[j] != nums[1 - 2]:
            nums[i] = nums[j]
            i += 1
    return i


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print(array_3_remove_duplicates(nums))

