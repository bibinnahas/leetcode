def remove_element(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


if __name__ == '__main__':
    print(remove_element([1, 2, 3, 4, 5, 5, 5, 6], 5))
