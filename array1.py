def merge(nums1, m, nums2, n):
    # Pointers for nums1, nums2, and the merged position (starting from the end)
    i, j, k = m - 1, n - 1, m + n - 1

    # Merge in reverse order
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # If any elements remain in nums2, copy them
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

    return nums1


if __name__ == '__main__':
    nums1 = [1, 4, 6, 0, 0, 0]
    nums2 = [2, 5, 7]
    m = 3
    n = 3
    print(merge(nums1, m, nums2, n))
