def remove_duplicates(nums):
    if not nums:
        return 0

    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            k += 1
    return k

if __name__ == '__main__':
    print(remove_duplicates([1, 2, 3, 4, 4, 5, 6, 7, 7, 8]))
