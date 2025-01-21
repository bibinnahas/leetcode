def atmost_two(nums):
    count = 1
    initial_pos = 1

    if not nums:
        return 0

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            count += 1
        else:
            count = 1
        if count <= 2:
            nums[initial_pos] = nums[i]
            initial_pos += 1

    return nums, initial_pos


if __name__ == '__main__':
    print(atmost_two([0, 1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 6]))
