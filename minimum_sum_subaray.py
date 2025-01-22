def min_subarray_len(nums, target):
    start = 0
    min_length = float('inf')
    current_sum = 0

    for end in range(len(nums)):
        current_sum += nums[end]

        while current_sum >= target:
            current_sum -= nums[start]
            min_length = min(min_length, end - start + 1)
            start += 1
    return min_length if min_length != float('inf') else 0


if __name__ == '__main__':
    print(min_subarray_len([1, 5, 1, 1, 1, 1], 7))
