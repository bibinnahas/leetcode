def remove_elem(nums, val):
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            k += 1
    return k

if __name__ == '__main__':
    nums = [3, 2, 2, 3, 4, 4, 3]
    val = 4

    print(remove_elem(nums, val))